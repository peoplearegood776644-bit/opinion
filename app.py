from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Questions load karne ka function
def load_questions():
    with open('questions.json') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    questions = load_questions()
    if request.method == 'POST':
        score = 0
        feedback = {}
        for i, q in enumerate(questions):
            selected = request.form.get(f"question-{i}")
            if selected == q['answer']:
                score += 1
            feedback[q['question']] = selected
        # Aap feedback yahan se save ya email kar sakte hain
        return render_template('result.html', score=score, total=len(questions))
    return render_template('quiz.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
