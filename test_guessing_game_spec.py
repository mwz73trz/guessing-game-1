# ----- DRIVER CODE -----
from guessing_game import GuessingGame
import random

game = GuessingGame(random.randint(0,100))
#can add GuessingGame(int(input("Guess: "))) to take a user input for the answer
last_guess  = None
last_result = None

while game.solved() == False:
  if last_guess != None: 
    print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    print("")

  last_guess  = int(input("Enter your guess: "))
  last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")

