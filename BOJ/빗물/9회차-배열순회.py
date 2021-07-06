h,w=map(int,input().split())
m=list(map(int,input().split()))
s=0
for i,d in enumerate(m):
    s+=min(max(m[:i+1]),max(m[i:]))-d
print(s)