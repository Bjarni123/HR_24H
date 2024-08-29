sidelength = int(input())

if sidelength != 1:
    print('* ' * (sidelength - 1) + "*")
    for x in range(sidelength-2):
        print('*', "  " * (sidelength-2) + '*')
    print('* ' * (sidelength - 1) + "*")
else:
    print('*')