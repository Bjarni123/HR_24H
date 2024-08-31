line1 = input()
line2 = input()
line3 = input()
line4 = input()

asciidifference = ord(line1[0]) - ord('H')



fullsentence = ''

for x in line1:
    charasciivalue = (ord(x) - asciidifference - 32) % 94 + 32
    print(charasciivalue)
    fullsentence += chr(charasciivalue)

fullsentence += '\n'

for x in line2:
    charasciivalue = (ord(x) - asciidifference - 32) % 94 + 32
    fullsentence += chr(ord(x) - asciidifference)

fullsentence += '\n'

for x in line3:
    charasciivalue = (ord(x) - asciidifference - 32) % 94 + 32
    fullsentence += chr(ord(x) - asciidifference)

fullsentence += '\n'

for x in line4:
    charasciivalue = (ord(x) - asciidifference - 32) % 94 + 32
    fullsentence += chr(ord(x) - asciidifference)

print(fullsentence)
