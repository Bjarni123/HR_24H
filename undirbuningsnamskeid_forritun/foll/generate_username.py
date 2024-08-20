def is_valid_name(name):
    for x in name:
        if (x.isalpha() or x.isspace()) == False:
            return False
    return True

def is_valid_year(year):
    for x in year:
        if x.isnumeric() == False:
            return False
    if 1900 <= int(year) <= 2022:
        return True
    else:
        return False

def generate_username(name, year):
    username = ""
    for x in name.split():
        if username == "":
            username += x
        else:
            username += x[0]
    username += year[-2:]
    return username

nafn = input("Enter in your name: ")
if is_valid_name(nafn):
    ar = input("Enter in your date of birth: ")
    if is_valid_year(ar):
        print("Your new username:", generate_username(nafn, ar))
    else:
        print("Invalid year of birth!")
else:
    print("Invalid name!")

