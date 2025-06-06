from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from utils.stt_assembly import transcribe_audio
import json
import os
import config
import uuid
from utils.json_handler import save_response
from utils.evaluator_gemini import evaluate_answer
from utils.report_generator import PDFReport
from pydub import AudioSegment
from flask import send_from_directory

app = Flask(__name__)

# Load questions from JSON
with open('questions.json', 'r') as file:
    questions = json.load(file)

# Track current question (in-memory)
user_progress = {
    "current": 0,
    "responses": []
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/interview')
def interview():
    q_num = user_progress["current"]
    if q_num >= len(questions):
        return redirect(url_for('summary'))
    return render_template('interview.html', question=questions[q_num], q_num=q_num+1, config=config)

@app.route('/dashboard')
def dashboard():
    with open('responses.json') as f:
        responses = json.load(f)

    scores = [resp.get('score', 0) for resp in responses]
    keywords = [len(resp.get('missing_keywords', [])) for resp in responses]
    total = len(scores)
    avg = round(sum(scores) / total, 2) if total > 0 else 0

    return render_template("dashboard.html",
        scores=scores,
        keywords=keywords,
        total_questions=total,
        avg_score=avg,
        responses=responses
    )

@app.route('/summary')
def summary():
    responses = user_progress["responses"]
    for resp in responses:
        evaluation = evaluate_answer(resp["question"], resp["answer"])
        resp["score"] = evaluation["score"]
        resp["feedback"] = evaluation["feedback"]
        resp["missing_keywords"] = evaluation.get("missing_keywords", [])

    with open("responses.json", "w") as f:
        json.dump(responses, f, indent=4)

    pdf_path = PDFReport(responses).generate()
    return render_template("final.html", results=responses, pdf_path=pdf_path)

@app.route('/transcribe_audio', methods=['POST'])
def transcribe():
    audio = request.files['audio']
    filename = f"{uuid.uuid4()}.webm"
    filepath = os.path.join("static", filename)
    audio.save(filepath)

    transcript = transcribe_audio(filepath)
    os.remove(filepath)

    return jsonify({"transcript": transcript})

@app.route('/save_audio', methods=['POST'])
def save_audio():
    audio = request.files['audio']
    q_num = request.form.get('q_num')
    filename = f"q{q_num}_{uuid.uuid4().hex}.mp3"
    webm_path = 'temp_audio.webm'
    mp3_path = os.path.join('static/audio', filename)

    audio.save(webm_path)
    sound = AudioSegment.from_file(webm_path, format="webm")
    sound.export(mp3_path, format="mp3")
    os.remove(webm_path)

    return jsonify({'success': True, 'filename': filename})

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    user_answer = request.form['transcript']
    audio_file = request.form.get('audio_file')
    q_index = user_progress["current"]
    question = questions[q_index]

    entry = {
        "question": question,
        "answer": user_answer,
        "audio_file": audio_file
    }

    user_progress["responses"].append(entry)
    user_progress["current"] += 1

    with open("responses.json", "w") as f:
        json.dump(user_progress["responses"], f, indent=4)

    if user_progress["current"] >= len(questions):
        return redirect(url_for('summary'))
    return redirect(url_for('interview'))

@app.route('/convert_mp3', methods=['POST'])
def convert_to_mp3():
    audio = request.files['audio']
    webm_path = 'temp_audio.webm'
    mp3_path = 'static/audio_output.mp3'

    audio.save(webm_path)
    sound = AudioSegment.from_file(webm_path, format="webm")
    sound.export(mp3_path, format="mp3")
    os.remove(webm_path)

    return jsonify({'success': True, 'file_path': mp3_path})

@app.route('/download_report/<filename>')
def download_report(filename):
    return send_from_directory("reports", filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)