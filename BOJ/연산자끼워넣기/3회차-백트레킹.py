import sys
maxR=-sys.maxsize
minR=sys.maxsize
def f(s,i,plus,minus,mul,div):
    global maxR, minR
    if plus<0 or minus<0 or mul<0 or div<0:
        return
    if i==(n-1):
        maxR=max(maxR,s)
        minR=min(minR,s)
        return
    f(s+A[i+1],i+1,plus-1,minus,mul,div)
    f(s-A[i+1],i+1,plus,minus-1,mul,div)
    f(s*A[i+1],i+1,plus,minus,mul-1,div)
    f(int(s/A[i+1]),i+1,plus,minus,mul,div-1)
n=int(input())
A=list(map(int,input().split(' ')))
signs=list(map(int,input().split(' ')))
f(A[0],0,signs[0],signs[1],signs[2],signs[3])
print(maxR)
print(minR)
        