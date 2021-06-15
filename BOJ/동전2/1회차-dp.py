#링크
'''
문제: https://www.acmicpc.net/problem/2294
참고:
'''
#풀이 법
'''
작은 것부터 누적시키며 조합이 k가 되는 수를 구한다.

1. 코인 가치가 큰 것을 우선 적용하는게 무조건 이득이다. `j%coins[i-1]==0:`
2. 처음에 현재값과 j/coin * coin하여 j기준 coin의 배수번째+그 남는 부분을 계산했으나  
dp[j]=min(dp[j],dp[int(j/coins[i-1])*coins[i-1]]+dp[j - int(j/coins[i-1])*coins[i-1]]) 어떤 경우에 반례가 있음(??)
어차피 개수를 구하는 것이니 위와 원리가 같지만 min(dp[j],dp[j-coins[i-1]]+1)와 같이 구현하는게 심플하고 반례가 없음

'''
#키포인트
'''
이차원 배열 구현시 시간초과 됨
'''

n,k=map(int,input().split())
dp=[10001 for _ in range(k+1)]
coins=[]
for _ in range(n):
    coins.append(int(input()))
coins.sort()
for i in range(1,n+1):
    for j in range(1,k+1):
        if j%coins[i-1]==0:
            dp[j]=j//coins[i-1]
        elif coins[i-1]<j:
            dp[j]=min(dp[j],dp[j-coins[i-1]]+1)
print(-1 if dp[k]==10001 else dp[k])