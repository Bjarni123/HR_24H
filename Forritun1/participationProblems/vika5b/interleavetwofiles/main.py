filename1 = input()
filename2 = input()
#with open(f'C:/Users/Bjarn/Documents/HR_24H/Forritun1/participationProblems/vika5b/interleavetwofiles/src/{filename1}', 'r') as file1, open(f'C:/Users/Bjarn/Documents/HR_24H/Forritun1/participationProblems/vika5b/interleavetwofiles/src/{filename2}' , 'r') as file2:

with open(f'/src/{filename1}', 'r') as file1, open(f'/src/{filename2}' , 'r') as file2:
    
    file1List = []
    for line in file1:
        file1List.append(line)

    file2List = []
    for line in file2:
        file2List.append(line)
    

    counter = 0
    while counter != max(len(file1List), len(file2List)):
        try:
            print(file1List[counter].strip())
        except:
            pass
        try:
            print(file2List[counter].strip())
        except:
            pass
        counter += 1