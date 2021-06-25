from itertools import combinations
n,k=map(int,input().split())
h={}
for i,c in enumerate('bdefghjklmopqrsuvwxyz'):
    h[c]=1<<i
words=[]
for _ in range(n):
    b=0
    for w in list(set(input()[4:-4]).difference('antic')):
        b|=h[w]
    words.append(b)
k-=5
if k<0:
    print(0)
    exit()
if k==26:
    print(n)
    exit()
ans=0
for comb in combinations([h[x] for x in h.keys()],k):
    s=sum(comb)
    cnt=0
    for w in words:
        if w&s==w:
            cnt+=1
    ans=max(ans,cnt)
print(ans)