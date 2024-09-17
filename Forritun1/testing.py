value = 127
delta = 0

if (value - delta) > 126:  # Ascii value is too high
    print((value - delta - 95), end="")
elif value - delta < 32:  # Ascii value is too low
    print((value - delta + 95), end="")
else:
    print((value - delta), end="")