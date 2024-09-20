import os
import time

desiredString = 'Hello World!!!'
currentOutput = ''
for character in desiredString:
    for asciicharidx in range(32, 127):
        print(currentOutput, end='')
        asciichar = chr(asciicharidx)
        if asciichar == character:
            currentOutput += asciichar
            print(asciichar)
            break
        print(asciichar)
        time.sleep(0.002)
        #os.system('cls')

print()