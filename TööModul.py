from MinuOmaModul import *
from Python_GMAIL import *
import os

def main():
    questions_file = "kusimused_vastused.txt"
    if not os.path.exists(questions_file):
        with open(questions_file, "w", encoding="utf-8"):
            pass

    questions = read_questions_answers(questions_file)

    candidates = []
    while True:
        candidate = interview(questions)
        candidates.append(candidate)
        choice = input("Jätka intervjuud? (jah/ei): ")
        if choice.lower() != "jah":
            break

    candidates.sort(key=lambda x: x[1], reverse=True)
    passed_candidates = [candidate for candidate in candidates if candidate[1] > len(questions) / 2]

    with open("oiged.txt", "w", encoding="utf-8") as file:
        for candidate in passed_candidates:
            file.write(f"{candidate[0]}: {candidate[1]}\n")

    with open("valed.txt", "w", encoding="utf-8") as file:
        for candidate in candidates:
            if candidate not in passed_candidates:
                file.write(f"{candidate[0]}: {candidate[1]}\n")

    print("\nTaotlusvorm on edukalt täidetud:")
    for candidate in passed_candidates:
        print(f"{candidate[0]}: {candidate[1]}")

    print("\nKeelatud:")
    for candidate in candidates:
        if candidate not in passed_candidates:
            print(f"{candidate[0]}: {candidate[1]}")

    add_question = input("Kas soovite failile küsimusi lisada? (jah/ei): ")
    if add_question.lower() == "jah":
        new_question = input("Sisestage uus küsimus: ")
        new_answer = input("Sisestage vastus uuele küsimusele: ")
        questions[new_question] = new_answer
        write_questions_answers(questions_file, {new_question: new_answer})

if __name__ == "__main__":
    main()

