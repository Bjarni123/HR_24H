import sys

guesses_counter = 0
lowerlimit = 0
upperlimit = 1001

while guesses_counter != 10:
    guess = (lowerlimit + upperlimit) // 2
    print(guess)
    sys.stdout.flush()
    result = input()
    if result == "correct":
        break
    elif result == "lower":
        upperlimit = guess
    else:
        lowerlimit = guess