# 🤖 AI Interview Simulator

An advanced voice-based technical interview simulator that evaluates your responses and provides real-time feedback with audio recording, AI-powered evaluation, detailed analytics, and PDF report generation.

---

## 🚀 Live Demo

[🔗 Click here to try the AI Interview Simulator (hosted on Render/Railway)](#)  
(*Replace `#` with your hosted link once deployed*)

---

## 🧠 Features

- 🎙️ Record voice answers for 10 real-world technical questions  
- 🧾 Auto-transcribe your speech using **AssemblyAI**  
- 🤖 Evaluate all answers using **Gemini Pro (Google AI Studio)**  
- 📈 Visual dashboard with score progression and keyword match stats  
- 📥 Downloadable PDF report with answer-level feedback  
- 🎧 Replay your recorded responses (stored as MP3)  
- 🔁 Restart interview anytime for practice  

---

## ⚙️ Tech Stack

| Component       | Tech Used |
|----------------|-----------|
| Backend         | Python, Flask |
| Frontend        | HTML, CSS (custom + Orbitron font), JavaScript |
| STT (Speech-to-Text) | [AssemblyAI API](https://www.assemblyai.com/) |
| Answer Evaluation | [Gemini API (Google AI Studio)](https://makersuite.google.com/) |
| Charting        | Chart.js |
| PDF Report      | FPDF |
| Audio Handling  | Pydub |
| Deployment      | Render / Railway |

---

## 🔄 Project Flow

Start Interview →
🎤 Record Answer →
📝 Transcribe Speech →
💾 Save MP3 + Text →
➡️ Go to Next Question →
📊 After Q10 → AI Evaluates All →
📄 Generate PDF Report →
📊 View Interactive Dashboard

## 📂 Folder Structure

ai_interview_simulator/
├── app.py
├── config.py
├── requirements.txt
├── responses.json
├── questions.json
├── static/
│ ├── audio/ # MP3 answers saved here
│ ├── recorder.js # Audio recorder + transcription trigger
│ └── style.css # Custom UI styling
├── templates/
│ ├── index.html
│ ├── interview.html
│ ├── result.html
│ ├── final.html
│ └── dashboard.html
├── utils/
│ ├── stt_assembly.py
│ ├── evaluator_gemini.py
│ ├── report_generator.py
│ └── json_handler.py
├── reports/ # PDF reports stored here


---

## 🔐 API Services Used

### 🎙️ AssemblyAI – Speech to Text  
- Converts `.webm` voice recordings to accurate English text  
- Used directly via JavaScript + Flask  
- [📌 Get your API key here](https://www.assemblyai.com)

### 🤖 Gemini Pro (Google AI Studio) – Text Evaluation  
- Evaluates technical answers for structure, keywords, and correctness  
- Responds with `score`, `feedback`, and `missing_keywords`  
- [📌 Use Gemini Studio](https://makersuite.google.com/) → Get your API key

---

## 📊 Example Charts

> Add screenshots here once deployed

![Score Chart](screenshots/score_chart.png)  
![Keyword Match](screenshots/keyword_match.png)

---

## 💻 How to Run Locally

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/ai-interview-simulator.git
cd ai-interview-simulator
2. **Set up a virtual environment**
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

Install dependencies
pip install -r requirements.txt

Set API keys
Create config.py and add:
GEMINI_API_KEY = "your_gemini_key"
ASSEMBLY_API_KEY = "your_assemblyai_key"

Run the app
python app.py

📄 License
MIT License. Use freely and improve it further!
Credit appreciated if you use this in your portfolio.

🙌 Acknowledgments
AssemblyAI – For accurate, fast speech-to-text
Google Gemini – For powerful NLP evaluation
Chart.js – For stunning analytics
FPDF – For smooth PDF generation

✨ Author
Glevin Roche
LinkedIn • GitHub • Portfolio (Add links)
