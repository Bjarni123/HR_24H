number_of_movies = int(input())
movies_sorted = sorted(list(map(int, input().split())))
movies_sorted = [str(x) for x in movies_sorted]

var1 = number_of_movies // 3
listi = movies_sorted[var1: var1 * 2] + movies_sorted[0:var1] + movies_sorted[var1 * 2:]
for x in listi:
    print(x, end=" ")
print()