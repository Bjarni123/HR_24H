line1 = input()
line2 = input()
line3 = input()
line4 = input()

asciidifference = ord(line1[0]) - ord('H')
numbers = []


fullsentence = ''

for line in [line1, line2, line3, line4]:
    for x in line:
        charasciivalue = (ord(x) - asciidifference - 32) % 95 + 32
        numbers.append(charasciivalue)
        print(chr(charasciivalue),end='')
    print()
