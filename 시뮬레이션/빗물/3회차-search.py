# 참조: 다른사람-search
#키포인트
'''
'''

def f(A):
    ans=0
    for i in range(len(A)):
        ans+=min(max(A[:i+1]),max(A[i:]))-A[i]
    return ans
input()
A=list(map(int,input().split(' ')))
print(f(A))      