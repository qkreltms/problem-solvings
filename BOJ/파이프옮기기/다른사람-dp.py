n = int(input())
house=[[] for _ in range(n)]
for i in range(n):
    house[i]=(list(map(int, input().split())))
pipe = [[[0,0,0] for _ in range(n)] for _ in range(n)]
pipe[0][1][0] = 1

for i, x in enumerate(pipe[0][2:]):
	if house[0][i+2]:
		break
	pipe[0][i+2][0] = pipe[0][i+1][0]

for i in range(1, n):
	for j in range(1, n):
		if house[i][j]: 
			continue
		pipe[i][j][0] = pipe[i][j-1][0]+pipe[i][j-1][1]
		pipe[i][j][2] = pipe[i-1][j][1]+pipe[i-1][j][2]
		if house[i-1][j] or house[i][j-1]:
			continue
		pipe[i][j][1] = sum(pipe[i-1][j-1])
print(sum(pipe[n-1][n-1]))