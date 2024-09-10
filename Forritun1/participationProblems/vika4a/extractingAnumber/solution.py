def extract_first_number_from_string(sentence):
    number = ''
    inNumber = False
    for letter in sentence:
        if letter.isnumeric():
            inNumber = True
            number += letter
        elif inNumber:
            break
    if inNumber:
        return int(number)
    else:
        return -1

