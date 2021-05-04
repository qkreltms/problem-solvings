def f(n, m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(i, m+1):
            if i == j:
                dp[i][j] = 1
            elif i == 1:
                dp[i][j] = j
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1] 
    return dp[n][m]

t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split(' ')))
    print(f(n, m))
    
