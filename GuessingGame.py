# Guessing Game - By Youssef Khaled
import random
print("=== Guess the Number Game ===")
number = random.randint(1, 10)
guess = int(input("Guess a number from 1 to 10: "))

if guess == number:
    print("You Win! 🎉")
else:
    print("Wrong! The number was", number)