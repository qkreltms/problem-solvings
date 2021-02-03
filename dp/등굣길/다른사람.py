'''
dp의 컨셉은 이전에 있던 값을 가져다 쓴다.
아래의 알고리즘은
3x3 지도일 때
한칸씩 늘려 모든 cell이 0으로 초기화된 4x4 지도로 만들어준다.
1,1에 1을 넣어준다.
0 0 0 0
0 1 0 0
0 0 0 0
0 0 0 0

1,1부터 4,4까지 순회하는데
순회하며 위, 왼쪽 셀의 값을 더해서 현재 셀에 넣어준다.(이전 값을 쓴다.)
그 후 m,n셀 값을 출력한다. 
2회)
0 0 0 0
0 1 1 0
0 0 0 0
0 0 0 0
3회)
0 0 0 0
0 1 1 1
0 0 0 0
0 0 0 0
4회)
0 0 0 0
0 1 1 1
0 1 0 0
0 0 0 0
5회)
0 0 0 0
0 1 1 1
0 1 2 0
0 0 0 0
n회)
0 0 0 0
0 1 1 1
0 1 2 3
0 1 3 6
'''

def solution(m, n, puddles):
    # 1부터 시작하는 (1,1) ~ (n, m) 2차원 배열
    memo = [[0 for _ in range(m+1)] for _ in range(n+1)]  # 0으로 초기화

    # 주의 ! - 문제에서 주어지는 row, col는 반대!
    for col, row in puddles:
        memo[row][col] = -1  # 갈수 없는 물 웅덩이 표시
    memo[1][1] = 1  # 출발 지점 1로 지정

    def dp(row, col):
        if row < 1 or col < 1 or memo[row][col] < 0:
            return 0
        # 이미 계산한 값이 있으면 값을 바로 가져옴
        if memo[row][col] > 0:
            return memo[row][col]

        memo[row][col] = dp(row, col-1) + dp(row-1, col)
        return memo[row][col]

    return dp(n, m) % 1000000007


# print(solution(2, 2, []), 2)
# print(solution(3, 3, []), 6)
# print(solution(3, 3, [[2, 2]]), 2)
# print(solution(3, 3, [[2, 3]]), 3)
# print(solution(3, 3, [[1, 3]]), 5)
# print(solution(3, 3, [[1, 3], [3, 1]]), 4)
# print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
# print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
# print(solution(1, 2, []), 1)
# print(solution(2, 1, []), 1)
# print(solution(2, 1, []), 1)
print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [
      4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0)
# print(solution(4, 4, [[3, 2], [2, 4]]), 7)
# print(solution(100, 100, []), 690285631)
# print(solution(100, 100, [[2, 2], [5, 5], [45, 45], [16, 76]]), 796186792)
