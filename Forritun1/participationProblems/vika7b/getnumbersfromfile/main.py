def main():
    with get_file() as file_obj:
        numbers = get_numbers_from_file(file_obj)
        display_numbers(numbers)


def get_file():
    """Gets file name from user and returns the open file handle.

    Asks the user repeatedly for file name
    until an existing file name is given.
"""

    keep_asking = True
    while keep_asking:
        filename = input()
        file_content = open_file(f'./src/{filename}')
        if file_content == None:
            print(f"{filename} not found! Please try again.")
        else:
            keep_asking = False
            return file_content

    # and implement this function.
    # You can call the following function in your implementation.


def open_file(filename: str):
    try:
        return open(filename)
    except FileNotFoundError:
        return None


def get_numbers_from_file(file) -> list:
    """Returns a list of all numbers in the given file.

    Assumes all numbers appear on their own,
    separated from other text by whitespace.
    """

    number_list = []

    for line in file:
        for element in line.split():
            try:
                number_list.append(int(element))
            except:
                pass

    return number_list


def display_numbers(numbers):
    """Prints out the list, after sorting it."""

    print(sorted(numbers))



if __name__ == "__main__":
    main()