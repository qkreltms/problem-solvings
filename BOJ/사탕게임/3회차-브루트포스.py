#키포인트
'''
변경이 발생한 행, 열만 순회해 시간 절약
예를 들어 첫 행의 Y,C가 바뀐다면 아래 처럼 순회한다.
YCPZY
CY
CC
YC
CP
단, 1,2회차와 다르게 전체 순회를 하지 않기 때문에 
swap에서 현재와 다음이 값이 같아도 순회해야한다.

*1,2회차에서는 0이 나옴
반례:
3
YYY
YYY
YYY
'''
n=int(input())
h=[[] for _ in range(n)]
ans=0
for i in range(n):
    h[i]=list(input())
def swap(i,j,flag):
    if flag:
        if h[i][j] == h[i+1][j]:
            return True
        h[i][j],h[i+1][j]=h[i+1][j],h[i][j]
    else:
        if h[i][j] == h[i][j+1]:
            return True
        h[i][j],h[i][j+1]=h[i][j+1],h[i][j]
def row(i):
    global ans
    cnt,w=0,h[i][0]
    for j in range(n):
        if w!=h[i][j]:
            w=h[i][j]
            ans=max(ans,cnt)
            cnt=1
        else:
            cnt+=1
    ans=max(ans,cnt) 
def col(j):
    global ans
    cnt,w=0,h[0][j]
    for i in range(n):
        if w!=h[i][j]:
            w=h[i][j]
            ans=max(ans,cnt)
            cnt=1
        else:
            cnt+=1
    ans=max(ans,cnt)
def check(i,j,flag):
    global ans
    swap(i,j,flag)
    if flag:
        row(i)
        row(i+1)
        col(j)
    else:
        row(i)
        col(j)
        col(j+1)
    swap(i,j,flag)
def f():
    for i in range(n):
        for j in range(n-1):
            check(j,i,True)
            check(i,j,False)
    return ans
    
print(f())