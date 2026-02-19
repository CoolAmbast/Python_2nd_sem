import random as rd
jackpot = rd.randint(1, 100)
attempts = 1
print("Welcome to the Number Guessing Game!")
while True:
    attempts += 1
    guess = int(input("Please enter a number between 1 and 100: "))
    if guess < 1 or guess > 100:
        print("Invalid input. Please enter a number between 1 and 100.")
        continue
    if guess < jackpot:
        print("Too low! Try again.")
    elif guess > jackpot:
         print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the correct number {jackpot} in {attempts} attempts!")
        break