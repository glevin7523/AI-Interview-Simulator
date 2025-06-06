import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-pro-latest')

def evaluate_answer(question, answer):
    prompt = f"""
You are an AI interview evaluator. Given the question and the candidate's answer, evaluate the response.

### Question:
{question}

### Answer:
{answer}

1. Score the answer from 0 to 10 (technical accuracy, clarity, and relevance).
2. Give 1-2 lines of constructive feedback.
3. List any important keywords or points that were missing.

Format your response as JSON like:
{{
  "score": 8,
  "feedback": "Clear and concise answer, but lacked detail on scalability.",
  "missing_keywords": ["load balancing", "horizontal scaling"]
}}
"""

    response = model.generate_content(prompt)
    try:
        # Parse structured response from Gemini
        output = response.text.strip().replace("```json", "").replace("```", "")
        return eval(output)
    except Exception as e:
        return {
            "score": 0,
            "feedback": "Evaluation failed.",
            "missing_keywords": []
        }
