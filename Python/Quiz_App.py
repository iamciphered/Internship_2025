# quiz_app.py

questions = {
    "What is the capital of France? ": "paris",
    "What is 5 + 7? ": "12",
    "Who wrote 'Romeo and Juliet'? ": "shakespeare",
    "What is the chemical symbol for water? ": "h2o"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question).strip().lower()
    if user_answer == answer:
        print(" Correct!")
        score += 1
    else:
        print(f" Wrong! The correct answer is {answer.capitalize()}.")

print(f"\nYour total score is {score}/{len(questions)}")
