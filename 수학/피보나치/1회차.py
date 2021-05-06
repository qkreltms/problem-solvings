#링크
'''
문제: https://www.acmicpc.net/problem/10870
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 
그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

참고:
'''
#풀이 법
'''
피보나치 3을 트리형식으로 그렸을 때 아래와 같다.
    3
  2   1
1  0
즉 바텀업 형식으로 dp로직을 표현하면 된다.
'''
#키포인트
'''
'''

def f(n):
    if n == 0:
        return 0
    dp=[0 for _ in range(n+1)]
    dp[1]=1
    for i in range(2, n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
n=int(input())
print(f(n))
    