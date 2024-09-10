def sum_of_range(start, end, step):
    sum = 0
    for x in range(start, end+1, step):
        sum += x
    return sum
