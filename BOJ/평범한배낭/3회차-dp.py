n, k = map(int, input().split())
bags = []
for _ in range(n):
    w, v = map(int, input().split())
    bags.append((w, v))
bags.sort(key=lambda x: x[0])
dp = [[0 for _ in range(k+1)] for _ in range(n)] # n+1안함, 왜냐면 어차피 마지막 인덱스가 비어있으므로 공간생성 낭비하지 말고 처음에만 공유하자
for i in range(n):
    for j in range(k+1):
        if j >= bags[i][0]:
            dp[i][j] = max(dp[i-1][j], bags[i][1]+dp[i-1][j-bags[i][0]])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n-1][k])


