import sys
n=int(input())
numArr=list(map(int,input().split()))
opers=list(map(int,input().split()))
minAns=sys.maxsize
maxAns=-sys.maxsize
def f(k,plus,minus,mul,div,res):
    global minAns, maxAns
    if plus<0 or minus<0 or mul<0 or div<0:
        return
    if k==n-1:
        maxAns=max(maxAns,res)
        minAns=min(minAns,res)
        return
    f(k+1,plus-1,minus,mul,div,res+numArr[k+1])
    f(k+1,plus,minus-1,mul,div,res-numArr[k+1])
    f(k+1,plus,minus,mul-1,div,res*numArr[k+1])
    f(k+1,plus,minus,mul,div-1,int(res/numArr[k+1]))
f(0,opers[0],opers[1],opers[2],opers[3],numArr[0])
print(maxAns)
print(minAns)