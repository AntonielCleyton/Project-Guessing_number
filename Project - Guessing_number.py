import random
import os
import time

class Verification:
    def __init__(self, name):
        self.name = name
        self.secret_number = random.choice(range(1, 10))

    def user_guess(self):
        attempts = 0
        while attempts != 3:
            print(self.secret_number)
            number = int(input('Choose a number from 1 to 10: '))
            if number == self.secret_number:
                print(f"You've guessed it, {self.name}! The number was: {self.secret_number}")
                return True
            else:
                print(f"Sorry, the correct number was: {self.secret_number} ")
                attempts += 1
                print(f'Number of attempts {attempts}.')
                print("Clearing the screen for a new attempt...")
                time.sleep(2)
                os.system('cls')
     

print("===Welcome to the Verification Game!===")
name = str(input("What's your name?\nAnswer: "))
user = Verification(name)
if user.user_guess():
    print("Winner!")
else:
    print("You lost")
