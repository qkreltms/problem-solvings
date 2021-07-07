#키포인트
'''
bfs가 시간초과 나고 dfs로도 풀 수 있다면, dfs로 풀어본다.
dfs가 속도가 더 빠르다.
'''
n=int(input())
h=[[] for _ in range(n)]
for i in range(n):
    h[i]=input().split()
if h[n-1][n-2] == '1' and h[n-2][n-1] == '1':
    print(0)
    exit()
cnt=0
# 3:대각선, 2:세로, 1:가로
def dfs(t, y,x):
    global cnt
    if y==n-1 and x==n-1:
        cnt+=1
        return
    if t==1:
        if x+1<n and h[y][x+1]!='1':
            dfs(1,y,x+1)
        if y+1<n and x+1<n and h[y+1][x+1]!='1' and h[y+1][x]!='1' and h[y][x+1]!='1':
            dfs(3,y+1,x+1)
    elif t==2:
        if y+1<n and h[y+1][x]!='1':
            dfs(2,y+1,x)
        if y+1<n and x+1<n and h[y+1][x+1]!='1' and h[y+1][x]!='1' and h[y][x+1]!='1':
            dfs(3,y+1,x+1)
    elif t==3:
        if x+1<n and h[y][x+1]!='1':
            dfs(1,y,x+1)
        if y+1<n and h[y+1][x]!='1':
            dfs(2,y+1,x)
        if y+1<n and x+1<n and h[y+1][x+1]!='1' and h[y+1][x]!='1' and h[y][x+1]!='1':
            dfs(3,y+1,x+1)
dfs(1,0,1)
print(cnt)

