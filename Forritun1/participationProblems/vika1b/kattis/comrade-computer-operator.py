current_temp = int(input())
prev_temp = int(input())

isRising = current_temp > prev_temp
isFalling = current_temp < prev_temp

if current_temp == 300:
    print('keep')

elif current_temp >= 350:
    print('shutdown')

elif current_temp < 300:
    if isRising:
        print('keep')
    else:
        print('raise')

elif not isFalling:
    print('lower')
else:
    print('keep')
    