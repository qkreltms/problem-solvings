n=int(input())
dp=[0,0,0,1,99,1,2,99]
if n==4 or n==7:
    print(-1)
    exit()
if n<8:
    print(dp[n])
    exit()
for i in range(8,n+1):
    dp.append(min(dp[i-3],dp[i-5])+1)
print(dp[n])