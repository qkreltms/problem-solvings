# 링크
'''
https://healingprocess.tistory.com/13
'''
import sys
input = sys.stdin.readline

n = int(input())

dp = [5000,5000,5000,1,5000,1,2,5000] 
if n<=7:
    if n==3 or n==5 or n==6:
        print(dp[n])
    else:
        print(-1)
    exit()
for i in range(8,n+1):
    temp = min(dp[i-3], dp[i-5])
    dp.append(temp+1)
if dp[n]>=5000:
    print(-1)
else:
    print(dp[n])