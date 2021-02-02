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
