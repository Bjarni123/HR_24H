wind_speed = float(input())

if wind_speed <= 0.2:
    print("Logn")
elif wind_speed <= 1.5:
    print("Andvari")
elif wind_speed <= 3.3:
    print("Kul")
elif wind_speed <= 5.4:
    print("Gola")
elif wind_speed <= 7.9:
    print("Stinningsgola")
elif wind_speed <= 10.7:
    print("Kaldi")
elif wind_speed <= 13.8:
    print("Stinningskaldi")
elif wind_speed <= 17.1:
    print("Allhvass vindur")
elif wind_speed <= 20.7:
    print("Hvassvidri")
elif wind_speed <= 24.4:
    print("Stormur")
elif wind_speed <= 28.4:
    print("Rok")
elif wind_speed <= 32.6:
    print("Ofsavedur")
else:
    print("Farvidri")