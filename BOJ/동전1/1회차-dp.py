#링크
'''
문제: https://www.acmicpc.net/problem/2293
참고: https://mong9data.tistory.com/68
'''
#풀이 법
'''
사진 참고
dp는 0~k일 때의 모든 조합을 누적하면서 구한다.
'''
#키포인트
'''
이차원 배열은 메모리 초과
'''

n,k=map(int,input().split())
coins=[int(input()) for _ in range(n)]
dp=[0 for _ in range(k+1)]
dp[0]=1
for c in coins:
    for i in range(c,k+1):
        if i-c>=0:
            dp[i]+=dp[i-c]
print(dp[k])