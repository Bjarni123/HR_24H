def is_valid_name(name):
    for x in name:
        if (x.isalpha() or x.isspace()) == False:
            return False
    return True

print(is_valid_name("Bjarni "))