def solution(w, h, puddles):
    myMap = [[0 for _ in range(w+1)] for _ in range(h+1)]
    myMap[1][1] = 1

    for x, y in puddles:
        myMap[y][x] = -1
    for y in range(1, h+1):
        for x in range(1, w+1):
            if y == 1 and x == 1:
                continue
            if myMap[y][x] == -1:
                myMap[y][x] = 0
                continue
            myMap[y][x] = myMap[y-1][x] + myMap[y][x-1]
    return myMap[h][w] % 1000000007

print(solution(2, 2, []), 2)
print(solution(3, 3, []), 6)
print(solution(3, 3, [[2, 2]]), 2)
print(solution(3, 3, [[2, 3]]), 3)
print(solution(3, 3, [[1, 3]]), 5)
print(solution(3, 3, [[1, 3], [3, 1]]), 4)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [
      4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0)
print(solution(4, 4, [[3, 2], [2, 4]]), 7)
print(solution(100, 100, []), 690285631)