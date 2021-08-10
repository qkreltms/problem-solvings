n,k=map(int,input().split())
dp=[0 for _ in range(k+1)]
coins=[]
for _ in range(n):
    coin=int(input())
    coins.append(coin)
dp[0]=1
for c in coins:
    for j in range(c,k+1):
        dp[j]+=dp[j-c]
print(dp[k])