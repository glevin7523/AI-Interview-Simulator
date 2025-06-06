import requests
import time
import os
from config import ASSEMBLY_API_KEY

def transcribe_audio(file_path):
    headers = {'authorization': ASSEMBLY_API_KEY}
    try:
        # Upload
        with open(file_path, 'rb') as f:
            upload_response = requests.post('https://api.assemblyai.com/v2/upload', headers=headers, files={'file': f})
        audio_url = upload_response.json()['upload_url']

        # Transcription request
        transcript_response = requests.post(
            'https://api.assemblyai.com/v2/transcript',
            headers=headers,
            json={'audio_url': audio_url}
        )
        transcript_id = transcript_response.json()['id']

        # Poll
        polling_url = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
        while True:
            polling_response = requests.get(polling_url, headers=headers).json()
            if polling_response['status'] == 'completed':
                return polling_response['text']
            elif polling_response['status'] == 'failed':
                return "Transcription failed."
            time.sleep(3)
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

