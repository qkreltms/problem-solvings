'''
문제에서 제시한대로 각 물건이 하나씩일 때
이 부분을 그 대로 사용하면 이전 물건의 최대 가치와 현재 물건의 최대 가치를 합친 값이 되고 
K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]], K[i-1][w]) 

이전 열이 아닌 현재 열로 바꾸면 각 물건이 n개 씩일 때까지 커버가 된다. (예: 1kg: 3가치가 W: 3일 때 원래의 3이아닌 9가된다.)  
K[i][w] = max(val[i-1]+K[i][w-wt[i-1]], K[i-1][w]) 

'''

def knapsack(W, wt, val, n):  # W: 배낭의 무게한도, wt: 각 보석의 무게, val: 각 보석의 가격, n: 보석의 수
    K = [[0 for x in range(W+1)] for x in range(n+1)]  # DP를 위한 2차원 리스트 초기화
    for i in range(n+1):
        for w in range(W+1):  # 각 칸을 돌면서
            if i==0 or w==0:  # 0번째 행/열은 0으로 세팅
                K[i][w] = 0
            elif wt[i-1] <= w:  # 점화식을 그대로 프로그램으로
                K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]], K[i-1][w])  # max 함수 사용하여 큰 것 선택
            # 현재 아이템의 무게가 더 크므로 이전 최대 가치를 그대로 쓴다.
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]

print(knapsack(4, [2], [2], 1), 2)
print(knapsack(30, [5,10,20], [5,6,14], 3), 20)