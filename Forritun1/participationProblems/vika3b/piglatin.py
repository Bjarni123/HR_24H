import sys

vowels = 'aeiuoy'

for line in sys.stdin:

    outputstring = ""

    for word in line.split():
        if word[0] in vowels:
            word += 'yay'
        else:
            while word[0] not in vowels:
                word = word[1:] + word[0]
            word += 'ay'
        outputstring += word + ' '

    print(outputstring)
