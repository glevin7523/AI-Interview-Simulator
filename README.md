# 🤖 AI Interview Simulator

An advanced voice-based technical interview simulator that evaluates your responses and provides real-time feedback with audio recording, AI-powered evaluation, detailed analytics, and PDF report generation.

---

## 🚀 Live Demo

[🔗 Click here to try the AI Interview Simulator (hosted on Render/Railway)](https://ai-interview-simulator-df4g.onrender.com)  

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

💻 **How to Run the Project Locally**
Follow these steps to set up and run the AI Interview Simulator on your machine:

**1️⃣ Clone the Repository**
git clone https://github.com/glevin7523/Ai-Interview-Simulator.git
cd ai-interview-simulator

**2️⃣ Set Up a Virtual Environment**
python -m venv venv
**Activate on Windows:**
venv\Scripts\activate
**Activate on Linux/macOS:**
source venv/bin/activate

**3️⃣ Install Dependencies**
pip install -r requirements.txt

**4️⃣ Add API Keys**
Create a config.py file and paste:
GEMINI_API_KEY = "your_gemini_api_key"
ASSEMBLY_API_KEY = "your_assemblyai_api_key"
🔗 Get Gemini API Key

🔗 Get AssemblyAI API Key

**5️⃣ Run the App**
python app.py
Then visit 👉 http://127.0.0.1:5000 to start your interview simulation!
________________________________________

**📄 License**

**MIT License**
Use this project freely for personal or commercial purposes. Contributions and credits are always welcome!
🙏 Please credit the author if you feature this in your portfolio or public demo.

---

**🙌 Acknowledgments**

Thanks to the amazing APIs and libraries that power this project:

🎙️ AssemblyAI – For real-time and accurate speech-to-text

🤖 Gemini (Google AI Studio) – For intelligent answer evaluation using NLP

📊 Chart.js – For dynamic analytics and dashboard visualizations

🧾 FPDF – For exporting performance feedback as PDF reports

---
**✨ Author**

**Glevin Roche**

💼 Passionate about building practical AI applications for real-world impact

- 🔗 [LinkedIn](https://www.linkedin.com/in/glevin-roche-27b754249/)
- 🔗 [GitHub](https://github.com/glevin7523)
- 🌐 [Portfolio](https://glevin-portfolio.vercel.app/)
  
