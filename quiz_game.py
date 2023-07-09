
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions_prompts = [
    "What is the capital of Australia?\n(a) Sydney\n(b) Canberra\n(c) Melbourne\n",
    "Which is the largest ocean?\n(a) Atlantic\n(b) Pacific\n(c) Indian\n",
    "Who invented Python programming language?\n(a) Guido van Rossum\n(b) Dennis Ritchie\n(c) James Gosling\n",
]

questions = [
    Question(questions_prompts[0], "b"),
    Question(questions_prompts[1], "b"),
    Question(questions_prompts[2], "a"),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You got {score}/{len(questions)} correct!")

run_quiz(questions)
