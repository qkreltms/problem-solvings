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
1#
7
38
810
2744
45265
위와 같이 있으면
젤 윗부분부터 시작해 level = 0, ..., n 이라하고
이 level을 1부터 재귀적으로 순회하면서 아래 2개의 자식에게
f(tree[level][i])
f(tree[level][i+1])
자신을 더한 값을 전달한다.
f(tree[level][i] + v)
f(tree[level][i+1] + v)

결과: 값은 맞지만(?=>왜냐면 부모가 2개일 때 최대 값을 쓰는게 보장되지 않음), 시간초과 발생
재귀함수로 처리한 것을 어떻게 while/for 문으로 변환하는가?
=> 재귀가 문제가 아니라 dp, 탐욕 방식을 쓰지 않음. => 다른사람2 확인

#2
7
38
810
2744
45265
위와 같이 있으면 #1 와 같은 로직을 적용했을 때 2명의 자식에게만 자신을 더한 값을 전달하기 까다로워진다.
해결 방법은 총 3개로 분리한다. [level][젤 첫번째 값], [level][마지막], [level][중간 값]이다. 단, 중간값을 부모에서 가장 큰 값을 가져온다.
'''


def solution(tri):
    for level in range(1, len(tri)):
        l = len(tri[level])
        for i in range(l):
            if i == 0:
                tri[level][i] += tri[level-1][i]
            if i == l-1:
                tri[level][i] += tri[level-1][l-2]
            if i != 0 and i != l-1:
                tri[level][i] += max(tri[level-1][i-1], tri[level-1][i])
    return max(tri[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]), 30)
print(solution(
    [[7], [3, 8], [8, 1, 3000], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
), 3025)
print(solution([[0], [0, 0], [0, 0, 0]]), 0)
print(solution([[0], [1, 0], [1, 0, 0]]), 2)
print(solution([[9999]]), 9999)


'''
#1 시간초과
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
