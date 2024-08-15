while True:
    file_fullname = input("Enter in a file name (or 'q' for quit): ")

    if file_fullname == "q":
        break

    filename, extension = file_fullname.split(".")
    
    if extension == "py":
        print("This is a Python file")
    elif extension == "cpp":
        print("This is a C++ file")
    elif extension == "js":
        print("This is a Javascript file")
    elif extension == "java":
        print("This is a Java file")
    else:
        print("Unknown extension")