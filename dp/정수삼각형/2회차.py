'''
'''


def solution(tree):
    height = len(tree)
    for curHeight in range(1, height):
        curWidth = len(tree[curHeight])
        for i in range(curWidth):
            if i == 0:
                tree[curHeight][0] += tree[curHeight-1][0]
            elif i == curWidth-1:
                tree[curHeight][curWidth-1] += tree[curHeight-1][curWidth-2]
            else:
                tree[curHeight][i] += max(tree[curHeight-1]
                                          [i-1], tree[curHeight-1][i])
    return max(tree[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]), 30)
print(solution(
    [[7], [3, 8], [8, 1, 3000], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
), 3025)
print(solution([[0], [0, 0], [0, 0, 0]]), 0)
print(solution([[0], [1, 0], [1, 0, 0]]), 2)
print(solution([[9999]]), 9999)
