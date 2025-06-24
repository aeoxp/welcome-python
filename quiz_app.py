# Storing questions and answers in a dictionary
quiz = {
    'questions': [
        {'text': 'What is 2 + 2?', 'answer': '4'},
        {'text': 'What is the capital of France?', 'answer': 'Paris'},
        {'text': 'What color do you get by mixing red and white?', 'answer': 'Pink'}
    ],
    'scores': {}
}

def ask_question(question):
    print(question['text'])
    return input("Your answer: ")

def check_answer(user_answer, correct_answer):
    if user_answer.lower().strip() == correct_answer.lower().strip():
        return True
    else:
        return False

def quiz_app():
    username = input("Enter your name: ")
    score = 0
    for question in quiz['questions']:
        user_answer = ask_question(question)
        if check_answer(user_answer, question['answer']):
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The correct answer was " + question['answer'])
    quiz['scores'][username] = score
    print(f"{username}, your score is {score}/{len(quiz['questions'])}.")

quiz_app()
