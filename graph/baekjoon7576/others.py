#import queue
from collections import deque
import sys

M,N = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
all_one = [[1]*M for _ in range(N)]

# 이미 다 익어있는 상태인지 검사
zero = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j]==0:
            zero += 1
if zero == 0:
    print(0)
else:
    #q = queue.Queue()
    q = deque()
    dx, dy = [-1,1,0,0], [0,0,-1,1]

    for i in range(N):
        for j in range(M):
            if tomato[i][j]==1:
                q.append((i,j))

    day = 0
    size = len(q)
    cnt = 0
    while len(q):
        if size==cnt:
            day += 1
            size=len(q)
            cnt = 0
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0<=new_x<N and 0<=new_y<M:
                if tomato[new_x][new_y] == 0:
                    tomato[new_x][new_y] = 1
                    q.append((new_x, new_y))


    # 익을 수 없는 토마토가 존재하는지 검사
    still_zero = 0
    for i in range(N):
        for j in range(M):
            if tomato[i][j]==0:
                still_zero += 1
    if still_zero == 0:
        print(day)
    else:
        print(-1)