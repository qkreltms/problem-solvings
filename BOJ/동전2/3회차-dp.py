n,k=map(int,input().split())
coins=[]
for _ in range(n):
    coins.append(int(input()))
dp=[100001 for _ in range(k+1)]
# 현재 알고리즘에서는 sort 필요, 단 2회차 처럼 sort없이도 가능
coins.sort()
for c in coins:
    for j in range(c,k+1):
        if j%c==0:
            dp[j]=j//c
        else:
            dp[j]=min(dp[j-c]+1,dp[j])
print(-1 if dp[k]==100001 else dp[k])
