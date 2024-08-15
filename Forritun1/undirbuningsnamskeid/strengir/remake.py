original_string = input("Enter in a string: ")

first2 = original_string[:2]
last2 = original_string[-2:]
string1 = first2 + last2
string2 = string1[::-1].lower().capitalize()

print(string2)