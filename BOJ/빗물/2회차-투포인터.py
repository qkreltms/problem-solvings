# 참조: 다른사람-투포인터
#키포인트
'''
디버깅을 잘 하자 lMax[1] 가 될 수가 없는데, 이 점을 보지를 못했다.
'''

def f(A):
    l,r,lMax,rMax,ans=0,len(A)-1,0,0,0
    while l<=r:
        if lMax <= rMax:
            lMax=max(lMax,A[l])
            ans+=lMax-A[l]
            l+=1
        else:
            rMax=max(rMax,A[r])
            ans+=rMax-A[r]
            r-=1
    return ans
input()
A=list(map(int,input().split(' ')))
print(f(A))