#링크
'''
문제: https://www.acmicpc.net/problem/1062
'''
#풀이 법
'''
a~z까지의 k개의 조합안에서 글자를 익혔을 때 최대 단어 읽음 횟수를 출력한다.
a-b-c-d,...
a-b-d-e,...
a-b-f-g,...
a-c-d-e,...
단, a-c-b,...와 같은 조합은 이미 앞에서 했으므로 필요없다.
위의 조합을 만들기 재귀적으로 순회하고 바로위의 조건을 만족시키기 위해 백트레킹 기법을 사용한다.

'''
#키포인트
'''
문제를 자의로 해석하지말자
N개의 단어와 k개의 "글자"가 있을 때 "최대" 몇 개의 단어를 읽을 수 있을까?
k개의 글자는 a,b,c,d,....를 말함

시간 초과
비트마스크를 쓰지 않으면 k개의 글자로 단어를 읽을 때 n^2의 소요시간이 걸림
사용하면 n 만에 가능 
'''

def g():
    r=0
    global m,visited
    for s in m:
        flag=True
        for c in s:
            if not visited[ord(c)-ord('a')]:
                flag=False
                break
        if flag:
            r+=1
    return r
def f(ai, cnt):
    global ans,k,visited
    if cnt == k:
        ans=max(ans,g())
        return
    for i in range(ai,26):
        if not visited[i]:
            visited[i]=True
            f(i,cnt+1)
            visited[i]=False
n,k=list(map(int,input().split(' ')))
m=[]
ans=0
visited=[False for _ in range(26)]
for _ in range(n):
    s=input()
    m.append(s[4:len(s)-4])
if k == 26:
    print(n)
    exit(0)
visited[ord('a')-ord('a')]=True
visited[ord('n')-ord('a')]=True
visited[ord('t')-ord('a')]=True
visited[ord('i')-ord('a')]=True
visited[ord('c')-ord('a')]=True
k-=5
if k<0:
    print(0)
    exit(0)
f(0,0)
print(ans)
