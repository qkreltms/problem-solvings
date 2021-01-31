'''
바텀업 형식으로 진행, 부모에 자식 중 가장 큰 값을 부모 값과 더해서 넣음
'''


def solution(triangle):
    memo = {}
    answer = f(triangle, 0, 0, memo)
    return answer


def f(triangle, i, j, memo):
    if i == len(triangle)-1:
        return triangle[i][j]

    if (i, j) in memo:
        return memo[(i, j)]

    a = f(triangle, i+1, j, memo)
    b = f(triangle, i+1, j+1, memo)
    x = triangle[i][j] + max(a, b)

    memo[(i, j)] = x

    return x


print(solution([[0], [1, 0], [1, 0, 0]]), 2)
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]), 30)
