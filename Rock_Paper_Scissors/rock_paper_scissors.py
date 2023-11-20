import random
import sys

class RPS:
    def __init__(self):
        print("Welcome to RPS 9000")
        self.moves: dict = {'rock': '🪨' ,'scissors' : '✂', 'paper':'📜'}
        self.valid_moves: list[str] = list(self.moves.keys())
        self.ai_score = 0
        self.your_score = 0

    def play_game(self):
        user_move:str = input("Rock, Paper, or scissors? >> ").lower()
        if user_move == "exit":
            print("THANKS FOR MOVING!")
            sys.exit()
        if user_move not in self.valid_moves:
            print("Invalid move")
            return self.play_game()

        ai_move:str = random.choice(self.valid_moves)
        self.display_moves(user_move, ai_move)
        self.check_move(user_move, ai_move)

    def display_moves(self, user_move:str, ai_move:str):
        print("----------")
        print(f"You {self.moves[user_move]}")
        print(f"AI {self.moves[ai_move]}")
        print("----------")

    def check_move(self, user_move:str, ai_move:str):

        if user_move == ai_move:
            print('It is a tie')
            #+print(f"The score is: your score is {your_score}, AI score is {ai_score}")
        elif user_move == 'rock' and ai_move =='scissors':
            self.your_score +=1
            print('You win')
            #print(f"The score is: your score is {your_score}, AI score is {ai_score}")
        elif user_move == 'scissors' and ai_move == 'paper':
            self.your_score += 1
            print('You win')
            #print(f"The score is: your score is {your_score}, AI score is {ai_score}")
        elif user_move == 'paper' and ai_move == 'rock':
            self.your_score += 1
            print('You win')
            #print(f"The score is: your score is {your_score}, AI score is {ai_score}")
        else:
            self.ai_score +=1
            print("AI wins...")
        print(f"The score is: your score is {self.your_score}, AI score is {self.ai_score}")


if __name__ == '__main__':
    rps = RPS()
    while True:
        rps.play_game()
