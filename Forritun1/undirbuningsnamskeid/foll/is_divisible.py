def is_divisable(a, b):
    return a % b == 0

agildi = int(input("Enter in a: "))
bgildi = int(input("Enter in b: "))

if is_divisable(agildi, bgildi):
    print(agildi, "is divisable by", bgildi)
else:
    print(agildi, "is not divisable by", bgildi)