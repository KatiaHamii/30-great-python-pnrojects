"""This bot will give an analysis according to its polarity"""

from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji : str
    sentiment: str


def get_mood(input_text: str, sensitivity: float) -> Mood:
    polarity: float = TextBlob(input_text).sentiment.polarity
    friendly_threashold: float = sensitivity
    hostile_trshold: float = -sensitivity

    if polarity >= friendly_threashold:
        return Mood('☺️', polarity)
    elif(polarity <= hostile_trshold):
        return Mood('😠', polarity)
    else:
        return Mood('😕', polarity)


def run_bot():
    print('Enter some text to get a sentiment analyso back:')
    while True:
        user_input: str = input("You: ")
        mood:Mood = get_mood(user_input, sensitivity=0.99)
        print("Bot: ", f'{mood.emoji}, {mood.sentiment}' )


if __name__ == '__main__':
    run_bot()

