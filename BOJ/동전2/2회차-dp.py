n,k=map(int, input().split())
coins=[]
for i in range(n):
    coins.append(int(input()))
dp=[10001 for _ in range(k+1)]
dp[0]=0
for i in range(n):
    for j in range(coins[i],k+1):
        dp[j]=min(dp[j],dp[j-coins[i]]+1)
print(-1 if dp[k]==10001 else dp[k])