tileMap = {
    11 : ["n"],
    12 : ["n","e","s"],
    13 : ["e","s"],
    21 : ["n"],
    22 : ["s","w"],
    23 : ["e","w"],
    31 : ["n"],
    32 : ["n","s"],
    33 : ["s","w"]

}

location = 11

while location != 31:
    availableDir = tileMap[location]
    directions = ''
    print('You can travel: ', end='')
    if 'n' in availableDir:
        directions += '(N)orth '
    if 'e' in availableDir:
        directions += '(E)ast '
    if 's' in availableDir:
        directions += '(S)outh '
    if 'w' in availableDir:
        directions+= '(W)est '

    directions = directions[:-1]
    directions = directions.replace(' ', ' or ')
    print(directions + '.')
    desiredDirection = input('Direction: ').lower()
    if desiredDirection in availableDir:
        if desiredDirection == 'n':
            location += 1
        elif desiredDirection == 'w':
            location -= 10
        elif desiredDirection == 's':
            location -= 1
        elif desiredDirection == 'e':
            location += 10
    else:
        print('Not a valid Direction!')

print('Victory!')

    
