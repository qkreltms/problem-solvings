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
