number = int(input("Enter in a number: "))

if number % 2 == 0 and number % 3 == 0:
    print("FizzBuzz")
elif number % 2 == 0:
    print("Fizz")
elif number % 3 == 0:
    print("Buzz")
else:
    print(number)
