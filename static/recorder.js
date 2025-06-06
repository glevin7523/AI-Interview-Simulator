mediaRecorder.onstop = async () => {
  status.textContent = "Processing...";

  const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
  const formData = new FormData();
  formData.append("audio", audioBlob);
  formData.append("q_num", "{{ q_num }}");

  // Save audio as MP3
  const saveRes = await fetch("/save_audio", {
    method: "POST",
    body: formData,
  });
  const saveData = await saveRes.json();
  const mp3Filename = saveData.filename;

  // Upload for transcription (AssemblyAI)
  const uploadRes = await fetch("https://api.assemblyai.com/v2/upload", {
    method: "POST",
    headers: {
      authorization: "{{ assembly_api_key }}"
    },
    body: audioBlob
  });
  const uploadData = await uploadRes.json();

  const transcriptRes = await fetch("https://api.assemblyai.com/v2/transcript", {
    method: "POST",
    headers: {
      authorization: "{{ assembly_api_key }}",
      "content-type": "application/json"
    },
    body: JSON.stringify({
      audio_url: uploadData.upload_url
    })
  });
  const transcriptData = await transcriptRes.json();

  let completed = false;
  let transcriptText = "";

  while (!completed) {
    const polling = await fetch(`https://api.assemblyai.com/v2/transcript/${transcriptData.id}`, {
      headers: { authorization: "{{ assembly_api_key }}" }
    });
    const pollingData = await polling.json();

    if (pollingData.status === "completed") {
      transcriptText = pollingData.text;
      completed = true;
    } else if (pollingData.status === "error") {
      transcriptText = "Transcription failed.";
      completed = true;
    } else {
      await new Promise(resolve => setTimeout(resolve, 2000));
    }
  }

  document.getElementById("transcriptBox").value = transcriptText;
  document.getElementById("transcriptInput").value = transcriptText;
  document.getElementById("status").textContent = "Transcription complete ✅";

  // Save filename to a hidden input if needed later
  const audioInput = document.createElement("input");
  audioInput.type = "hidden";
  audioInput.name = "audio_file";
  audioInput.value = mp3Filename;
  document.querySelector("form").appendChild(audioInput);
};
