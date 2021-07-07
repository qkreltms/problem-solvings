#링크
'''
문제: https://www.acmicpc.net/problem/17070
참고:

* 시간초과 발생
'''
#풀이 법
'''
미로찾기 형식을 푼다.
'''
#키포인트
'''
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
def bfs(pipeType, startY,startX):
    global cnt
    q=[(pipeType,startY,startX)]
    while q:
        t,y,x=q.pop(0)
        if y==n-1 and x==n-1:
            cnt+=1
            continue
        if t==1:
            if x+1<n and h[y][x+1]!='1':
                q.append((1,y,x+1))
            if y+1<n and x+1<n and h[y+1][x+1]!='1' and h[y+1][x]!='1' and h[y][x+1]!='1':
                q.append((3,y+1,x+1))
        elif t==2:
            if y+1<n and h[y+1][x]!='1':
                q.append((2,y+1,x))
            if y+1<n and x+1<n and h[y+1][x+1]!='1' and h[y+1][x]!='1' and h[y][x+1]!='1':
                q.append((3,y+1,x+1))
        elif t==3:
            if x+1<n and h[y][x+1]!='1':
                q.append((1,y,x+1))
            if y+1<n and h[y+1][x]!='1':
                q.append((2,y+1,x))
            if y+1<n and x+1<n and h[y+1][x+1]!='1' and h[y+1][x]!='1' and h[y][x+1]!='1':
                q.append((3,y+1,x+1))
bfs(1,0,1)
print(cnt)

