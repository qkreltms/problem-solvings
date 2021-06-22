n=int(input())
if n<5:
    if n==3:
      print(1)
    else:
      print(-1)
    exit()
dp=[0 for _ in range(n+1)]
dp[0]=1
for bag in [3,5]:
    for j in range(bag,n+1):
        if j%bag==0:
            dp[j]=j//bag
        elif dp[j-bag]==0:
            continue
        else:
            dp[j]=dp[j-bag]+1
print(-1 if dp[n]==0 else dp[n])