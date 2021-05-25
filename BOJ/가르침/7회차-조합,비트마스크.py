#키포인트
'''
list(combinations())
list있고 없고가 메모리 차이(80000=>30000), 성능(2400ms => 2300ms) 차이 유의미함
destructing할 수 있으면 하는게 좋음 
'''
from string import ascii_lowercase
from itertools import combinations
n,k=map(int,input().split())
h={}
words=[]
ans,visited=0,0
for i,c in enumerate(set(ascii_lowercase)-set('antic')):
    h[c]=1<<i
for _ in range(n):
    b=0
    for w in input()[4:-4]:
        if not w in 'antic':
            b|=h[w]
    words.append(b)
k-=5
if k<0:
    print(0)
    exit(0)
if k==26:
    print(n)
    exit(0)
sources=[]
for i in range(21):
    sources.append(1<<i)
for comb in combinations(sources,k):
    cur=sum(comb)
    cnt=0
    for w in words:
        if cur&w==w:
            cnt+=1
    ans=max(ans,cnt)
print(ans)