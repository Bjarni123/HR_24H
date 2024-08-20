height = int(input("How tall are you in cm: "))

if height < 0:
    print("Invalid height!")
elif height < 140:
    print("You are not tall enough for the rollercoaster")
else:
    print("You are tall enough to ride the rollercoaster")