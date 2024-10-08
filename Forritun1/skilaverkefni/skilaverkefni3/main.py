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



# Constants

FILE_LOCATION = './src/'
AVAILABLE_COMMANDS = ['l', 's', 'a', 'w', 'q']
QUIT = 'q'

# Functions

def get_file(filename):
    """takes the filename and returns the file in a list or None if the file is not found"""

    # Try to open the file, if successful, return the file as a list, otherwise return None
    try:
        file_content = []
        with open(FILE_LOCATION + filename, 'r') as file:
            file_content = [line.strip() for line in file]
        
        return file_content
    except:
        return None



def get_command_and_argument(line):
    """Takes a string and splits it up by the / sign and returns the correct command and argument(None if none is given)"""

    # Try to split the line
    try:
        command, argument = line.split('/')
    except ValueError:
        # If Value Error then see if the command has an argument and if it is a command.
        if line in AVAILABLE_COMMANDS:
            # If it is a command I return the command with the argument as None
            return line, None
        else:
            # If it is not a command I return None for both
            return None, None
    
    # If the command is not available then return None for both
    if command not in AVAILABLE_COMMANDS:
        return None, None
    
    # Otherwise I return both the command and argument
    return command, argument

def l_command(file, line_number):
    """Takes in the file as a list and which line it wants. If the line_number is out of range or not a number, then return 'Invalid line number'"""
    
    # Check if the line number is a digit and within the available range. and return accordingly
    if line_number.isdigit() and 0 < int(line_number) < (len(file) + 1):
        return file[int(line_number) - 1]
    else:
        return 'Invalid line number!'

def s_command(file, argument):
    """Takes in file as a list and the argument. to search for, Then returns all line that starts with argument"""
    
    lines_with_argument = []
    for line in file:
        if line.startswith(argument):
            lines_with_argument.append(line)

    return "\n".join(lines_with_argument)

def a_command(file, argument):
    """Takes in file as a list and the argument, then adds the argument to the list and returns it"""
    file.append(argument)
    return file

def w_command(file_content, filename):
    """Takes in the file as a list and the filename, then writes the content of the file into the file with that filename"""
    with open(FILE_LOCATION + filename, 'w') as file:
        file.writelines("\n".join(file_content))




# Main program



file = None
filename = ''

# Get the filename from user and if the file does not exist, then exit the program.

filename = input("Enter filename: ")
file = get_file(filename)

if file == None:
    print('File not found!')
    exit()



# Create a loop to keep asking for commands until user decides to quit
command = ''
while command != QUIT:
    the_input = input('Enter Action: ')

    # Take the input and split it into the command and argument
    command, argument = get_command_and_argument(the_input)

    # Check if the argument is None and it is not w(since the w command is run by itself with no arguments)
    if argument == None and command != 'w':
        continue

    # Call the correct function and print it out according to the command. 
    match command:
        case 'l':
            l_result = l_command(file, argument)
            print(l_result)
        
        case 's':
            s_result = s_command(file, argument)
            print(s_result)
        
        case 'a':
            file = a_command(file, argument)

        case 'w':
            w_command(file, filename)
            print('File written!')

        case _:
            continue
