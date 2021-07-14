#링크
'''
문제: https://www.acmicpc.net/problem/2606
참고:
'''
#풀이 법
'''
'''
#키포인트
'''
1-2
1-3
으로 가는 것도 있지만
2-1
3-1
로 가는것도 있을 수 있다.
'''

n=int(input())
e=int(input())
h=[[] for _ in range(n+1)]
visited=[False for _ in range(n+1)]
visited[1]=True
for i in range(e):
    a,b=map(int,input().split())
    h[a].append(b)
    h[b].append(a)

cnt=0
def dfs(sn):
    global cnt
    for i in h[sn]:
        if not visited[i]:
            cnt+=1
            visited[i]=True
            dfs(i)
dfs(1)
print(cnt)