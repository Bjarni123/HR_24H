classroom_amount, sanitizer_amount = input().split()
needed_sanitizers = 0
for classroomIdx in range(int(classroom_amount)):
    classroom_need = int(input())
    needed_sanitizers += classroom_need

if int(sanitizer_amount) - needed_sanitizers < 0:
    print('Neibb')
else:
    print('Jebb')