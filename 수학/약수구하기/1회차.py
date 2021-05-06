#링크
'''
문제: https://www.acmicpc.net/problem/2501
자연수 n, k가 주어질 때 n의 약수 중 k번째 작은 수는?
만약 k보다 개수가 작으면 0 출력
약수란 n을 m(m<=n)으로 나눌 때 나머지가 0인 m
'''
#풀이 법
'''
'''
#키포인트
'''
'''
n, k = list(map(int, input().split(' ')))
def f():
    dp=[]
    for i in range(1, n+1):
        if n%i==0:
            dp.append(i)
    dp.sort()
    if len(dp) < k:
        return 0
    return dp[k-1]
print(f())
