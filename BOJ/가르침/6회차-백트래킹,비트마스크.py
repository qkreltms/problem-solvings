#키포인트
'''
처음에 
for i,a in enumerate(ascii_lowercase):
    if not a in antic:
        h[a]=1<<i
이렇게 했는데 이렇게 하면 i가 여러번 건너뛰는 경우가 발생한다. 1,2,4,5,...
반면 visited는 1,2,3,4,... 순으로 체크를 해주므로 틀린답이 나오게된다.
'''
n,k=map(int,input().split())
h={}
antic='antic'
words=[]
alphabets = 'bdefghjklmopqrsuvwxyz'
for i, c in enumerate(alphabets):
    h[c] = 1<<i
for _ in range(n):
    b=0
    for w in input()[4:-4]:
        if not w in antic:
            b|=h[w]
    words.append(b)
k-=5
if k<0:
    print(0)
    exit(0)
if k==26:
    print(n)
    exit(0)
ans,visited=0,0
def g():
    cnt=0
    for w in words:
        if w&visited==w:
            cnt+=1
    return cnt
def f(ai,cnt):
    global ans,visited
    if cnt==k:
        ans=max(ans,g())
        return
    for i in range(ai,21):
        visited|=(1<<i)
        f(i+1,cnt+1)
        visited&=~(1<<i)
f(0,0)
print(ans)