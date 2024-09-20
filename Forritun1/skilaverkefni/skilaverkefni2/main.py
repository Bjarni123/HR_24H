# fall til þess að búa til lista með playerposition
def makeMap(playerPos, maplength):
    tempMap = ['x' for x in range(maplength)]
    tempMap[playerPos-1] = 'o'
    return tempMap

# Hér prenta ég út kortið og spyr spilarann hvaða átt hann vill fara
def printmap_getdir():
    kort = makeMap(position, endPoint)
    print("".join(kort))
    print("""l: left\nr: right""")
    desiredDir = input("Move: ").lower()
    return desiredDir

# Hreyfi spilarann í valdna átt. Ef hann er út í enda, þá skila ég upprunalega staðsetningunni
def moveposition(desiredDir, position):
    if desiredDir == 'l':
        if position != startPoint:
            return position - 1
        else:
            return position
    elif desiredDir == 'r':
        if position != endPoint:
            return position + 1
        else:
            return position
    return position





position = 0

desiredDir = 'l'

R = 1
L = -1

startPoint = 1
endPoint = 10


# While loopu til þess að fá byrjunar staðsetningu innan leyfilegra markra.
while not(startPoint <= position <= endPoint):
    position = int(input(f'Position in [{startPoint}..{endPoint}]: '))

# Meðan inputtinn eru annaðhvort l eða r þá færi ég player position miðað við hvað var valið
while desiredDir == 'l' or desiredDir == 'r':
    desiredDir = printmap_getdir()
    position = moveposition(desiredDir, position)
    


