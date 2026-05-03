import random

easy_quiz = {
    "2 + 2?": "4",
    "10 - 2?": "8"
}

hard_quiz = {
    "5 * 6?": "30",
    "Capital of Uganda?": "Kampala",
    "Capital of Kenya?": "Nairobi"
}

difficulty = input("Choose difficulty (easy/hard): ").lower()

if difficulty == "easy":
    quiz = easy_quiz
else:
    quiz = hard_quiz

questions = list(quiz.items())
random.shuffle(questions)

score = 0

for question, answer in questions:
    print("Answer quickly!")
    user_answer = input(question + " ")

    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answer}")

    print()

print(f"Final score: {score}/{len(questions)}")
