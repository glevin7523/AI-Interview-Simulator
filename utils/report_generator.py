from fpdf import FPDF
import datetime

class PDFReport:
    def __init__(self, data):
        self.data = data
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def generate(self):
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(200, 10, txt="AI Interview Evaluation Report", ln=True, align='C')
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(200, 10, txt=f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True)

        for idx, entry in enumerate(self.data):
            self.pdf.ln(10)
            self.pdf.set_font("Arial", 'B', 14)
            self.pdf.cell(200, 10, txt=f"Question {idx+1}:", ln=True)
            self.pdf.set_font("Arial", size=12)
            self.pdf.multi_cell(0, 10, f"{entry['question']}")
            self.pdf.set_text_color(0, 102, 204)
            self.pdf.multi_cell(0, 10, f"Answer: {entry['answer']}")
            self.pdf.set_text_color(0, 0, 0)
            self.pdf.multi_cell(0, 10, f"Score: {entry.get('score', '-')}/10")
            self.pdf.multi_cell(0, 10, f"Feedback: {entry.get('feedback', 'N/A')}")
            if entry.get("missing_keywords"):
                self.pdf.multi_cell(0, 10, f"Missing Keywords: {', '.join(entry['missing_keywords'])}")
            if entry.get("audio_file"):
                self.pdf.multi_cell(0, 10, f"Audio File: static/audio/{entry['audio_file']}")

        filename = f"reports/report_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
        self.pdf.output(filename)
        return filename
