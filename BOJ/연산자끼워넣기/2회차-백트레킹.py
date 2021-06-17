def f(plus,minus,mul,div,i,s):
    global N, maxR, minR, nums
    if plus<0 or minus<0 or mul<0 or div<0:
        return
    if i==N:
        maxR=max(maxR,s)
        minR=min(minR,s)
        return
    f(plus-1,minus,mul,div,i+1,s+nums[i])
    f(plus,minus-1,mul,div,i+1,s-nums[i])
    f(plus,minus,mul-1,div,i+1,s*nums[i])
    f(plus,minus,mul,div-1,i+1,int(s/nums[i]))
N=int(input())
nums=list(map(int,input().split(' ')))
gihos=list(map(int,input().split(' ')))
maxR=-1000000000
minR=-maxR
f(*gihos,1,nums[0])
print(maxR)
print(minR)