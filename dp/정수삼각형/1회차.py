# 문제
'''
7
38
810
2744
45265
위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 
아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 
예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.
삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

삼각형의 높이는 1 이상 500 이하입니다.
삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.
'''
# 문제풀이
'''

'''
'''
# 시간초과 => dp를 쓸 때가 왔다.
def f(i, level, v):
    if level == lastLevel:
        ans.append(v)
        return
    f(i, level+1, tree[level][i]+v)
    f(i+1, level+1, tree[level][i+1]+v)


def solution(triangle):
    global ans
    global lastLevel
    global tree
    tree = triangle
    ans = []
    lastLevel = len(triangle)
    f(0, 1, triangle[0][0])
    return max(ans)
'''


def solution(triangle):
    lastLevel = len(triangle)
    dp = [0 for _ in range(lastLevel+1)]
    dp[0] = triangle[0][0]
    for level in range(1, lastLevel+1):
        for i in range(len(triangle[level])):
            dp[level] = triangle[level][i] + dp[level-1]


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]), 30)
print(solution([[7], [3, 8], [8, 1, 3000], [
      2, 7, 4, 4], [4, 5, 2, 6, 5]]), 3025)
print(solution([[0], [0, 0], [0, 0, 0]]), 0)
print(solution([[0], [1, 0], [1, 0, 0]]), 2)
print(solution([[9999]]), 9999)
