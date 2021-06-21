h,w=map(int,input().split())
blocks=list(map(int,input().split()))
def f():
    ans=0
    for i,b in enumerate(blocks):
        ans+=min(max(blocks[:i+1]),max(blocks[i:]))-b
    return ans
print(f())
        