# 키포인트
'''
https://healingprocess.tistory.com/13
'''
n=int(input())
if n < 8:
    if n==3 or n==5:
        print(1)
    elif n==6:
        print(2)
    else:
        print(-1)
    exit(0)
dp=[0 for _ in range(n+1)]
dp[1],dp[2],dp[3],dp[4],dp[5],dp[6],dp[7]=99,99,1,99,1,2,99
for i in range(8,n+1):
    dp[i]=min(dp[i-3],dp[i-5])+1
print(-1) if dp[n] == 0 else print(dp[n]) 