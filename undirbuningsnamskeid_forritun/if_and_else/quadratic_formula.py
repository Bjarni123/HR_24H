a_str = input("Enter a: ") # Do not remove this line
b_str = input("Enter b: ") # Do not remove this line
c_str = input("Enter c: ") # Do not remove this line

# Enter your solution below
a = int(a_str)
b = int(b_str)
c = int(c_str)

d = d = b**2 - 4 * a * c

if d < 0:
    print("The equation has 0 roots")
elif d == 0:
    print("The equation has 1 root")
else:
    print("The equation has 2 roots")

