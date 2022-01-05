# This is a game where you guess a random number between 1 and 50!
import random 

for i in range(1):
    value = random.randint(1, 50)

    a = int(input("Guess a Number Between 1 and 50: "))

    if a==value:
      print("Your Guess is Correct!")

    elif a!=value:
      print("Your Guess is Wrong!")
      print("Correct Number was", value) #Tells the correct for the number