hometeam_name = input("Enter the home team's name: ")
awayteam_name = input("Enter the away team's name: ")
hometeam_score = 0
awayteam_score = 0

while True:
    who_scored = input("What team scored?: ")
    if who_scored == hometeam_name:
        hometeam_score += 1
    elif who_scored == awayteam_name:
        awayteam_score += 1
    elif who_scored == "done":
        break
    else:
        print("That team is not playing, try again")


if hometeam_score == awayteam_score:
    print("It's a draw {}-{}".format(hometeam_score, awayteam_score))
elif hometeam_score < awayteam_score:
    print("{} won {}-{}".format(awayteam_name, awayteam_score, hometeam_score))
else:
    print("{} won {}-{}".format(hometeam_name, hometeam_score, awayteam_score))
