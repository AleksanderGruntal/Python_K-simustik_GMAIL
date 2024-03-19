def read_questions_answers(file_name):
    questions = {}
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            question, answer = line.strip().split(":")
            questions[question.strip()] = answer.strip()
    return questions

def write_questions_answers(file_name, questions):
    with open(file_name, "a", encoding="utf-8") as file:
        for question, answer in questions.items():
            file.write(question + ":" + answer + "\n")

def interview(questions):
    name = input("Tere! Mis su nimi on? ")
    print(f"Tere, {name}!")
    score = 0
    for question, answer in questions.items():
        user_answer = input(f"{name}, {question}: ")
        if user_answer.lower() == answer.lower():
            print("Õige!")
            score += 1
        else:
            print("Vale.")
    return name, score


