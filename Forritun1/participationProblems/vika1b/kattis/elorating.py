elo = int(input())

if elo < 1000:
    print("Invalid")
elif elo < 2400:
    print("Amateur")
elif elo < 2500:
    print("International grandmaster")
elif elo < 2700:
    print("Grandmaster")
else:
    print("Super grandmaster")