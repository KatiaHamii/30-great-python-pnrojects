from difflib import get_close_matches
import json


def get_best_matches(user_input:str, questions:str )-> str| None :
    questions: list[str] = [q for q in questions]
    matches: list[str] = get_close_matches(user_input, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]
    else:
        return None


def chatbot(knowledge: dict):
    while True:
        user_input: str = input(str("You: "))
        best_match: str | None = get_best_matches(user_input, knowledge)

        answer= knowledge.get(best_match)
        if answer:
            print(answer)

        else:
            print ("Sorry, i dont understand you!")


if __name__ == "__main__":
    file: dict = "questions.json"
    with open(file, "r", encoding="utf-8") as file:
        data = json.load(file)
    #dialog: dict = {"hello": "Hey hey",
   #                 "how are you": "i am fine",
   #                 "what is your name?" : "i dont know",
    #                "bye": "bye bye"}
    chatbot(data)
