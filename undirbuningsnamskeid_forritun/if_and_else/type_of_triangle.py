sideA = int(input("Enter in the first side of the triangle: "))
sideB = int(input("Enter in the second side of the triangle: "))
sideC = int(input("Enter in the third side of the triangle: "))

if sideA == sideB == sideC:
    print("This is a equilateral triangle")
elif sideA == sideB or sideA == sideC or sideB == sideC:
    print("This is an isoceles triangle")
else:
    print("This is a scalene triangle")