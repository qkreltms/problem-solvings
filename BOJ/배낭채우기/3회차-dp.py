n,k=map(int,input().split())
bags=[0 for _ in range(n)]
for i in range(n):
    w,v=map(int,input().split())
    bags[i]=(w,v)
bags.sort(key=lambda x:x[0])
dp=[[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1,n+1):
  for j in range(k+1):
    if bags[i-1][0] <= j:
      dp[i][j]=max(dp[i-1][j], bags[i-1][1]+dp[i-1][j-bags[i-1][0]])
    else:
      dp[i][j]=dp[i-1][j]
print(dp[n][k])