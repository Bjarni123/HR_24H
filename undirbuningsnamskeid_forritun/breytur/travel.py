meters = float(input("How many meters did you travel: "))
minutes = int(input("How long did it take in minutes?: "))

km = meters / 1000
hours = minutes / 60

speed = km / hours

print("You were traveling {}km/h".format(round(speed, 2)))