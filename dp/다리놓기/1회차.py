# 링크
'''
문제: https://www.acmicpc.net/problem/1010
참고:
'''
# 풀이 법
'''
'''
# 키포인트
'''
'''


def p():
    def f(n, m):
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(i, m+1):
                # n, m이 서로 같으면 규칙에 의해서 1이 된다.
                if i == j:
                    dp[i][j] = 1
                # n = 1이고 m = N개가 되면 무조건 m개수를 따라간다.
                elif i == 1 and j > i:
                    dp[i][j] = j
                # 
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
        return dp[n][m]
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split(' '))
        print(f(n, m))


p()
