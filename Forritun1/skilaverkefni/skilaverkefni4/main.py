"""

This is the main code

I used a few functions only once, but it made the code more readable.

While grading this, please recommend further ways to improve my code

Things i wasn't sure about:
    Use of function(especially using them once)
    Is there a better way to handle data in and out of functions
    Should i create function to only use inside functions

"""
# Constants ----------------------------------------------------------------------------------------------------------------------------

import pathlib
main_py_dir = (pathlib.Path(__file__).parent.resolve())

FILES_LOCATION = f'{main_py_dir}/src/' 

# Classes ------------------------------------------------------------------------------------------------------------------------------


# Functions ----------------------------------------------------------------------------------------------------------------------------

def print_option_screen():
    """Prints out the option screen"""

    print()
    print("1. Show constituencies")
    print('2. Show parties')
    print('3. Show results')
    print("9. Quit")
    print()

    return

def open_file(filename):
    """Opens a file from filename and returns a list of all the lines stripped"""

    file_content = None

    try:
        with open(FILES_LOCATION + filename, 'r') as file:
            file_content = [line.strip() for line in file]

        return file_content
    except FileNotFoundError:
        return None


"""                                               Function for constituencies and parties                                            """

def get_value_sum(data):
    """Takes in a dictionary and returns the sum of all the values."""

    the_sum = sum([int(value) for value in data.values()])

    return the_sum

def load_list_if_empty(the_list):
    """If list alrady exists, return it. Otherwise, format it correctly for constituencies and parties. returns it in dictionary"""
    
    # Return the list if it already exists
    if the_list:
        return the_list

    # Get filename and open it
    filename = input('File name: ')
    file = open_file(filename)

    # if it fails then return None
    if not file:
        return None
    
    # Put the file into a dictionary.
    file_dict = {}
    for line in file:
        file_key, file_value = line.split(';')
        file_dict[file_key] = file_value

    # Return a copy of the file, so future data doesn't screw up past data
    return file_dict.copy()

def print_2_table_headers(table_name_1, table_name_2, header_width_1, header_width_2):
    """Takes in 2 header names and prints them out with approriate spacing"""
    
    print(table_name_1.ljust(header_width_1) + table_name_2.rjust(header_width_2))
    print('-' * (header_width_1 + header_width_2))

    return

def print_2_columns(data, column1_width, column2_width):
    """Takes in dictionary of data and prints it out in a table format with appropriate spacing"""

    for key, value in data.items():
        print(f"{key.ljust(column1_width)}{value.rjust(column2_width)}")

    return

def print_constituency_table(data, column1_name, column2_name, column1_width, column2_width):
    """Prints out the constituency table"""

    # Print for Kattis
    print()

    # Call the oppropriate functions with correct arguments to print out table.
    print_2_table_headers(column1_name, column2_name, column1_width, column2_width)
    print_2_columns(data, column1_width, column2_width)

    # Print out the table tail
    print('-' * (column1_width + column2_width))
    the_sum = get_value_sum(data)
    print("Total:".ljust(column1_width) + str(the_sum).rjust(column2_width))

def print_parties_table(data, column1_name, column2_name, column1_width, column2_width):
    #Print for Kattis
    print()

    # Print out the table
    print_2_table_headers(column1_name, column2_name, column1_width, column2_width)
    print_2_columns(data, column1_width, column2_width)

    return


"""                                                         Function for results                                                        """

def load_results_if_empty(the_results):
    """Loads the result table if it doesn't already exists and returns it a dictionary with tuple as value"""

    # Have a seperate function for this, since the formatting is different

    # If the results already exists, return them
    if the_results:
        return the_results

    # Get filename and open the file
    filename = input('File name for results: ')
    try:
        file = open_file(filename)

        # Create the necessary variables
        file_content = {}
        last_key = ''

        # Go through the file
        for line in file:

            # If line is empty, I skip
            if not line:
                continue

            # I try to split up the line
            try:
                the_list, party = line.split(';')
                # If successful I but the list and party in a set and add it to the last key(constituency)
                the_set = (the_list, party)
                file_content[last_key].append(the_set)
            except:
                # If the split fails, then its a constituency and i add it to the dictionary and update the last key variable.
                file_content[line] = list()
                last_key = line
        
        return file_content

    except:
        # If an error occurs, I return None
        return None

def get_total_sums(the_results):
    """Return the sum of the votes"""
    votes_sum = 0

    for result_tuple in the_results:
        votes_sum += int(result_tuple[1])
    
    return votes_sum

def print_results_table_header(the_constituency):
    # Prints out the result table header with the appropriate constituency name
    print(the_constituency)
    print('List'.ljust(10) + 'Party'.rjust(26) + 'Votes'.rjust(10) + 'Ratio'.rjust(10))
    print('-' * 56)

def calculate_ratio_and_print_results_table(the_constituency, total_votes, parties):
    """Calculate the total ratio and prints out the table contents"""

    ratio_sum = 0

    # Go throught the data
    for result_tuple in the_constituency:
            # Create the table content
            list_letter = result_tuple[0]
            votes = int(result_tuple[1])
            ratio = (votes / total_votes) * 100
            party = parties[list_letter]

            # Print out the table content
            print(f'{str(list_letter).ljust(10)}{str(party).rjust(26)}{str(votes).rjust(10)}{str(round(ratio, 1)).rjust(10)}')
            
            # Add it to the total ratio
            ratio_sum += ratio

    # Then return it
    return ratio_sum

def print_results_tail(total_votes, total_ratio, turnout):
    """Gets the result table tail(bottom of the table). arguments are the total votes, ratio and the turnout."""
    print('-' * 56)
    print('Total:'.ljust(36) + f'{str(total_votes).rjust(10)}' + '{:.1f}'.format(total_ratio).rjust(10))
    print('Turnout:'.ljust(46) + '{:.1f}'.format(turnout).rjust(10))

def collection_table(the_constituencies, the_parties, the_results, constituency):
    """Prints out the collection table"""

    # Have a try except, I don't use it in this code, but possible to see if printing out the collection table is successfull
    try:
        
        results_from_constituency = the_results[constituency]


        # Find the sum
        total_votes = get_total_sums(results_from_constituency)
        
        total_ratio = 0

        # Print for Kattis
        print()
        # Print out the header
        print_results_table_header(constituency)

        # Calculate total ratio and turnout
        total_ratio = calculate_ratio_and_print_results_table(results_from_constituency, total_votes, the_parties)
        turnout = round(total_votes / int(the_constituencies[constituency]) * 100, 1)

        # prints out the table tail.
        print_results_tail(total_votes, total_ratio, turnout)

        return True
    except:
        return False




# Main ------------------------------------------------------------------------------------------------------------------------------------


def main():
    constituencies = None
    parties = None
    results = None

    option = 0

    while option != 9:

        print_option_screen()
        option = int(input("Select an action: "))

        match option: 

            case 1: # Show Constituencies
                # Create the list if it doesn't exist, then start over
                constituencies = load_list_if_empty(constituencies)

                # If it is successful, then print the table
                if constituencies:
                    print_constituency_table(constituencies, 'Constituency', 'Electorals', 20, 10)
            
            case 2: # Show Parties
                # Same logic as in showing constituencies
                parties = load_list_if_empty(parties)

            
                if parties:
                    print_parties_table(parties, 'List', 'Party', 6, 26)
            case 3: # Show Result
                # Load the results
                results = load_results_if_empty(results)

                # If all data is available then ask for the constituency and print out the table
                if constituencies and parties and results:
                    constituency = input('Constituency: ')
                    collection_table(constituencies, parties, results, constituency)
                else:
                    # If not all data is available then put results to None again
                    results = None

            case _:
                # If anything else is selected I skip
                pass
            

main()