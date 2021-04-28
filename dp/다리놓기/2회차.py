def f():
    def solution(n, m):
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(i, m+1):
                if i == 1:
                    dp[i][j] = j
                elif i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
        return dp[n][m]
    t = int(input())
    for _ in range(t):
        n, m = list(map(int, input().split(' ')))
        print(solution(n, m))
f()