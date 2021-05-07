#링크
'''
문제: https://www.acmicpc.net/problem/2581
소수를 구하고 M,N 범위의 소수 최소값, 합을 출력하라

참고:
'''
#풀이 법
'''
'''
#키포인트
'''
'''

def f(n):
    h=[True for _ in range(n+1)]
    h[1]=False
    for i in range(2, int(n**0.5)+1):
        if h[i]:
            for j in range(i*2, n+1, i):
                h[j]=False
    return h
m=int(input())
n=int(input())
A=[]
h=f(n)
for i, v in enumerate(h[m:n+1]):
    if v:
        A.append(m+i)
if not A:
    print(-1)
else:
    print(sum(A))
    print(A[0])