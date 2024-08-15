import random

random.seed(1) # Þessi lína er svo að vefsíðan getur prófað lausnina. Ekki eyða

number_to_guess = random.randint(1, 100)

# Implement your solution below

guess = -4321
while guess != number_to_guess:
    guess = int(input("Guess a number in the range 1-100: "))
    if guess < number_to_guess:
        print("The number is larger")
    elif guess > number_to_guess:
        print("The number is smaller")
    else:
        print("You are correct, the number was {number_to_guess}!".format(number_to_guess=number_to_guess))