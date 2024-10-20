'''

This is the first code, in the file main.py is the commented and more optimized code for readability

'''
# Constants ----------------------------------------------------------------------------------------------------------------------------

FILES_LOCATION = '/src/' 
#                './Forritun1/skilaverkefni/skilaverkefni4/src/'

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

def get_file(filename):
    """takes the filename and returns the file in a list or None if the file is not found"""

    # Try to open the file, if successful, return the file as a list, otherwise return None
    try:
        file_content = {}
        with open(FILES_LOCATION + filename, 'r') as file:
            for line in file:
                line_content_1, line_content_2 = line.strip().split(';')
                file_content[line_content_1] = line_content_2


            # file_content = [line.strip().split(';') for line in file]
        
        return file_content
    except:
        return None

def load_results_if_empty(the_results):
    
    if not the_results:
        filename = input('File name for results: ')
        try:
            file_content = {}
            with open(FILES_LOCATION + filename, 'r') as file:
                last_key = ''
                for line in file:

                    if not line:
                        continue


                    line_stripped = line.strip()
                    try:
                        the_list, party = line_stripped.split(';')
                        the_set = (the_list, party)
                        file_content[last_key].append(the_set)
                    except:
                        file_content[line_stripped] = list()
                        last_key = line_stripped
            
            return file_content

        except:
            return None

    return the_results


def load_list_if_empty(the_list):
    # If the file does not exist, create it
    if not the_list:
        # Get filename and open the file
        filename = input('File name: ')
        the_list = get_file(filename)
    return the_list

def print_constituency_table(data, column1_name, column2_name, column1_width, column2_width):

    print()

    print(column1_name.ljust(column1_width) + column2_name.rjust(column2_width))
    print('-' * (column1_width + column2_width))
    
    for key, value in data.items():
        print(f"{key.ljust(column1_width)}{value.rjust(column2_width)}")
    
    print('-' * (column1_width + column2_width))
    
    the_sum = get_value_sum(data)
    print("Total:".ljust(column1_width) + str(the_sum).rjust(column2_width))


def print_parties_table(data, column1_name, column2_name, column1_width, column2_width):

    print()

    print(column1_name.ljust(column1_width) + column2_name.rjust(column2_width))
    print('-' * (column1_width + column2_width))
    
    for key, value in data.items():
        print(f"{key.ljust(column1_width)}{value.rjust(column2_width)}")


    return

def get_value_sum(data):
    """Takes in a dictionary and returns the sum of all the values."""

    the_sum = sum([int(value) for value in data.values()])

    return the_sum

def create_collection(constituencies_data, parties_data, results_data):
    the_collection = {}
    the_collection["Constituencies"] = constituencies_data
    the_collection["Parties"] = parties_data
    the_collection["Results"] = results_data

    return the_collection

def collection_table(the_constituencies, the_parties, the_results, constituency):
    try:
        
        results_from_constituency = the_results[constituency]


        # Find the sum
        total_votes = 0
        for result_tuple in results_from_constituency:
            total_votes += int(result_tuple[1])

        total_ratio = 0

        print()

        print(constituency)
        print('List'.ljust(10) + 'Party'.rjust(26) + 'Votes'.rjust(10) + 'Ratio'.rjust(10))
        print('-' * 56)

        for result_tuple in results_from_constituency:
            list_letter = result_tuple[0]
            votes = int(result_tuple[1])
            ratio = (votes / total_votes) * 100
            party = the_parties[list_letter]

            print(f'{str(list_letter).ljust(10)}{str(party).rjust(26)}{str(votes).rjust(10)}{str(round(ratio, 1)).rjust(10)}')
            
            total_ratio += ratio

        print('-' * 56)
        print('Total:'.ljust(36) + f'{str(total_votes).rjust(10)}' + '{:.1f}'.format(total_ratio).rjust(10))

        turnout = round(total_votes / int(the_constituencies[constituency]) * 100, 1)

        print('Turnout:'.ljust(46) + '{:.1f}'.format(turnout).rjust(10))

        return True
    except:
        return False




# Main ------------------------------------------------------------------------------------------------------------------------------------

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

            if constituencies:
                print_constituency_table(constituencies, 'Constituency', 'Electorals', 20, 10)
        
        case 2: # Show Parties
            parties = load_list_if_empty(parties)

        
            if parties:
                print_parties_table(parties, 'List', 'Party', 6, 26)
        case 3: # Show Result
            results = load_results_if_empty(results)

            if constituencies and parties and results:
                constituency = input('Constituency: ')
                collection_table(constituencies, parties, results, constituency)
            else:
                results = None

        case _:
            pass
        

