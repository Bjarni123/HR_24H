problems = input().split(';')
total_problems = 0

for problem in problems:
    if '-' in problem:
        start_end_prob = problem.split('-')
        total_problems += int(start_end_prob[1]) - (int(start_end_prob[0]) - 1)
    else:
        total_problems += 1

print(total_problems)