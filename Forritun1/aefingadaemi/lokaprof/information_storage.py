def open_file():
    file_content = dict()
    try:
        with open('information_storage_file.txt', 'r') as file:
            for line in file:
                name, value = line.split()
                file_content[name] = value
        return file_content
    except:
        return {'length': 0.0, 'width': 0.0, 'height': 0.0, 'mass': 0.0, 'volume': 0.0}       

def write_file(file_content):
    with open('information_storage_file.txt', 'w+') as file:
        for name, value in file_content.items():
            file.write(f'{name} {value}\n')

values = open_file()

choice = 0
while choice != 'exit':

    for name, value in values.items():
        print(f'{name}\t{value}')

    choice = input('Enter Action: ')

    try:
        name, value = choice.split()
        if name.lower() in values:
            values[name] = float(value)
    except:
        if choice == 'exit':
            write_file(values)

