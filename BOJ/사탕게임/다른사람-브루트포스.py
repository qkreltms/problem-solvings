#키포인트
'''
변경이 발생한 행, 열만 순회해 시간 절약
예를 들어 첫 행의 Y,C가 바뀐다면 아래 처럼 순회한다.
YCPZY
CY
CC
YC
CP
'''

def row(graph, x, y):
    cnt = 1
    py = y+1
    my = y-1
    while py < N:
        if graph[x][py] == graph[x][y]:
            cnt += 1
            py += 1
        else:
            break
    while 0 <= my:
        if graph[x][my] == graph[x][y]:
            cnt += 1
            my -= 1
        else:
            break
    return cnt

def col(graph, x, y):
    cnt = 1
    px = x+1
    mx = x-1
    while px < N:
        if graph[px][y] == graph[x][y]:
            cnt += 1
            px += 1
        else:
            break
    while 0 <= mx:
        if graph[mx][y] == graph[x][y]:
            cnt += 1
            mx -= 1
        else:
            break
    return cnt

N = int(input())
graph = [list(input()) for i in range(N)]
dx = [1,0]
dy = [0,1]
Max = 1
for x in range(N):
    for y in range(N):
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
                a = col(graph, x, y)
                b = col(graph, nx, ny)
                c = row(graph, x, y)
                d = row(graph, nx, ny)
                Max = max(Max, a, b, c, d)
                graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
print(Max)