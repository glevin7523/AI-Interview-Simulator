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

---

## 💻 How to Run the Project Locally

Follow the steps below to get started with the AI Interview Simulator on your local machine:

### 🔁 1. Clone the Repositoryj

```bash
git clone https://github.com/yourusername/ai-interview-simulator.git
**cd ai-interview-simulator**

