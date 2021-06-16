#링크
'''
문제: https://www.acmicpc.net/problem/1978
주어진 수들 중 소수의 개수를 출력한다
4
1 3 5 7

참고:
'''
#풀이 법
'''
에라토스테네스의 체를 구현해 놓고 인덱스로 접근해 값을 출력한다.

'''
#키포인트
'''
python의 range는 int 값만 허용된다.
'''

def f(n):
    h=[True for _ in range(n+1)]
    h[1]=False
    for i in range(2, int(n**0.5)+1):
        if h[i] == True:
            for j in range(i*2,n+1,i):
                h[j]=False
    return h
t=int(input())
A=list(map(int, input().split(' ')))
n = max(A)
h = f(n)
cnt = 0
for i in A:
    if h[i] == True:
        cnt+=1
print(cnt)

