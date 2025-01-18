from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move
def get_move(num):
    if num == 1:
        return rock
    elif num == 2:
        return paper
    else:
        return scissors

computer = get_move(num)

def get_user_move():
    return input("Enter your move (1- rock,2- paper, or 3- scissors): ")

# Ask a user to enter their move
user_move = get_user_move()
while not user_move.isdigit():
    user_move = get_user_move()

user_move = get_move(int(user_move))

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
print(f"Your move: {user_move}")

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print(f"Computer move: {computer}")

# Figure out who wins and print the result!
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif user == rock:
        if computer == scissors:
            return "You win!"
        else:
            return "Computer wins!"
    elif user == paper:
        if computer == rock:
            return "You win!"
        else:
            return "Computer wins!"
    elif user == scissors:
        if computer == paper:
            return "You win!"
        else:
            return "Computer wins!"
        
print(determine_winner(user_move, computer))