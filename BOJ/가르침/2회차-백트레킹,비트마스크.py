def g():
    res=0
    for w in words:
       if (visited & w) == w:
            res+=1
    return res
def f(ai, cnt):
    global ans,visited
    if cnt==k:
        ans=max(ans, g())
        return
    for i in range(ai, 21):
        if not visited & (1<<i):
            visited|=(1<<i)
            f(i, cnt+1)
            visited&=~(1<<i)
h = {}
for i,c in enumerate('bdefghjklmopqrsuvwxyz'):
    h[c]=i
visited=0
ans=0
words=[]
n,k=list(map(int, input().split(' ')))
for _ in range(n):
    s=input()[4:-4]
    w=0
    for c in s:
        # antic에 해당되지 않은 값만 단어로 저장한다.
        # antic에 해당되는 값은 무시하거나(이전 값으로), 0을 넣는다.
        if not c in 'antic':
            w|=(1<<h[c])
    words.append(w)
k-=5
if k==26:
    print(0)
    exit(0)
if k<0:
    print(0)
    exit(0)
f(0,0)
print(ans)
    
        