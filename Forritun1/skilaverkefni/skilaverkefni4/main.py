'''
Hafa lýsandi nöfn á ensku á breytum.  Ekki gefa breytum nöfn sem eru notuð fyrir innbyggð tög (eins og int, float, bool, str).
Forðast að nota sama breytunafn til að geyma gildi af mismunandi tagi.
Setja bil á milli breytna og virkja í setningum og segðum (space between variables and operators in statements and expressions).
Setja inn auðar línur í kóða á völdum stöðum (t.d. á milli fallaskilgreininga) til að forritstextinn sé ekki of samþjappaður.
Setja inn athugasemdir (comment) þar sem við á.  Þó ekki ofnota því oft gildir "the code is the comment".
Gott að fylgja þessari reglu: Rule 6: If it was hard to write, it is probably hard to read.  Add a comment.
Fjarlægja óþarfa kóða.
Einfalda flókinn kóða.
Endurtaka ekki runu af sama kóða.
Nota ekki while True: og break ef auðvelt er að skrifa skilyrði sem stýrir því hvenær while-lykkjan hættir. 
Nota fasta þar sem við á
Nota ekki global breytur.  Sendið alltaf gildi inni í fall ef fall þarf á gildi breytu að halda.
Láta setningar aðalforrits vera á einum stað (ekki hér og þar inn á milli fallaskilgreininga). 
Láta kóða inn í try-blokk aðeins vera þann sem villa getur komið upp í (og er gripin með except).
Brjóta forrit upp í einstakar einingar með notkun falla.  
Láta sérhvert fall hafa skýrt og einfalt hlutverk. Rule 8: A function should do one thing.   Skrifa docstring fyrir sérhvert fall.
Ekki láta fall kalla á quit() / exit().
Endurtaka ekki (nánast) sama kóða.  Frekar kalla oftar en einu sinni á fall sem framkvæmir viðkomandi aðgerð.
'''
# Constants ----------------------------------------------------------------------------------------------------------------------------

FILES_LOCATION = './skilaverkefni/skilaverkefni4/src/' 
#                './src/'

# Classes ------------------------------------------------------------------------------------------------------------------------------

# Functions ----------------------------------------------------------------------------------------------------------------------------

def print_option_screen():
    """Prints out the option screen"""
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

    print(column1_name.ljust(column1_width) + column2_name.rjust(column2_width))
    print('-' * (column1_width + column2_width))
    
    for key, value in data.items():
        print(f"{key.ljust(column1_width)}{value.rjust(column2_width)}")
    
    print('-' * (column1_width + column2_width))
    
    the_sum = get_value_sum(data)
    print("Total:".ljust(column1_width) + str(the_sum).rjust(column2_width))

def print_parties_table(data, column1_name, column2_name, column1_width, column2_width):

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

def collection_table(the_constituencies, the_parties, the_results):
    table = []
    table = add_list_and_party_collumn(the_parties)


    return

def add_list_and_party_collumn(the_parties):
    """Takes the parties dictionary and puts them into 2 different columns for table"""
    list_column = []
    party_column = []
    
    for party_letter, party_name in the_parties.items():
        list_column.append(party_letter)
        party_column.append(party_name)

    
    the_columns = [{"Party": list_column}, {"List": party_column}]

    return the_columns





# Main ------------------------------------------------------------------------------------------------------------------------------------

constituencies = None
parties = None
results = None

option = 0

while option != 9:

    print_option_screen()
    option = input()

    match int(option): 
        case 1: # Show Constituencies
            # Create the list if it doesn't exist, then start over
            constituencies = load_list_if_empty(constituencies)

            if not constituencies:
                pass

            print_constituency_table(constituencies, 'Constituency', 'Electorals', 20, 10)
        case 2: # Show Parties
            parties = load_list_if_empty(parties)

            if not parties:
                pass

            print_parties_table(parties, 'List', 'Party', 6, 26)
        case 3: # Show Result
            results = load_results_if_empty(results)

            if not results:
                pass
            
            collection = create_collection(constituencies, parties, results)
            collection_table(constituencies, parties, results)
        case _:
            pass
        

