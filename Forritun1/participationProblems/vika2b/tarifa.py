X = int(input())
N = int(input())
totalData = X*(N+1)

for i in range(N):
	usedData = int(input())
	totalData -= usedData

print(totalData)
