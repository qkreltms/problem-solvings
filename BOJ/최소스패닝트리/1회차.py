#링크
'''
문제: https://www.acmicpc.net/problem/1197
'''
#풀이 법
'''
크루즈칼 + find(트리 납작하게 만듦)
'''
#키포인트
'''
'''

v,e=map(int,input().split())
paths=[]
root=[i for i in range(v+1)]
for _ in range(e):
    x,y,c=list(map(int,input().split()))
    paths.append([x,y,c])
def union(r1,r2):
    if r1 < r2:
        root[r2]=r1
    else:
        root[r1]=r2
def find(x):
    if root[x] != x:
        root[x]=find(root[x])
    return root[x]
def f():
    ans=0
    for x,y,c in sorted(paths, key=lambda x:x[2]):
        r1=find(x)
        r2=find(y)
        if r1 != r2:
            union(r1,r2)
            ans+=c
    return ans
print(f())