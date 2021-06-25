n,k=map(int,input().split())
words=[]
h={}
for i,c in enumerate('bdefghjklmopqrsuvwxyz'):
    h[c]=1<<i
for _ in range(n):
    w=list(set(input()[4:-4])-set('antic'))
    b=0
    for c in w:
        b|=h[c]
    words.append(b)
k-=5
if k<0:
    print(0)
    exit(0)
if k==26:
    print(n)
    exit(0)
ans=0
visited=0
def g():
    cnt=0
    for w in words:
        if visited & w == w:
            cnt+=1
    return cnt
def f(si, cnt):
    global ans, visited
    if cnt==k:
        ans=max(g(), ans)
        return
    for i in range(si, 21):
        visited|=1<<i
        f(i+1, cnt+1)
        visited&=~1<<i
f(0,0)
print(ans)
    
    