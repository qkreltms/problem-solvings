'''
'''


def solution(N, K, iw, iv):
    table = [[0 for _ in range(K+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, K+1):
            if iw[i-1] <= j:
                table[i][j] = max(table[i-1][j], iv[i-1]+table[i-1][j-iw[i-1]])
            else:
                table[i][j] = table[i-1][j]
    return table[N][K]

print(solution(4, 12, [3,4,5,6], [6,8,12,13]))
# print(solution(1, 4, [2], [2]), 2)
# print(solution(3, 30, [5, 10, 20], [5, 6, 14]), 20)
