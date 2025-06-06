import json
import os

RESP_FILE = 'responses.json'

def save_response(question, answer):
    entry = {
        "question": question,
        "answer": answer
    }

    if not os.path.exists(RESP_FILE):
        with open(RESP_FILE, 'w') as file:
            json.dump([entry], file, indent=4)
    else:
        with open(RESP_FILE, 'r+') as file:
            data = json.load(file)
            data.append(entry)
            file.seek(0)
            json.dump(data, file, indent=4)
