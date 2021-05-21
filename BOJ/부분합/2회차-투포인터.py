import sys
n,s=list(map(int,input().split()))
seqs=list(map(int,input().split()))
def f():
    i,j,ans,subSeq=0,0,sys.maxsize,0
    while True:
        if subSeq>=s:
            ans=min(ans,i-j)
            subSeq-=seqs[j]
            j+=1
        elif n<=i:
            break 
        else:
            subSeq+=seqs[i]
            i+=1
            continue
        if i==j:
            return 1
    return 0 if ans == sys.maxsize else ans 
print(f())
        