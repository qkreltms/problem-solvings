from itertools import combinations
from string import ascii_lowercase
n,k=list(map(int,input().split(' ')))
words,h=[],{}
notantic=set(ascii_lowercase)-set('antic')
for i,c in enumerate(notantic):
    h[c]=1<<i
for _ in range(n):
    bit=0
    for c in input()[4:-4]:
        if not c in 'antic':
            bit|=h[c]
    words.append(bit)
sources=[]
for i in range(21):
    sources.append(2**i)
k-=5
if k<0 or k==26:
    print(0)
    exit(0)
ans=0
for comb in list(combinations(sources, k)):
    cnt=0
    r=sum(comb)
    for w in words:
        if w & r == w:
            cnt+=1
    ans=max(ans,cnt)
print(ans)
    