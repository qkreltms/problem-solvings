# 문제
'''
지도의 m, n 크기, 가지 못하는 영역이 주어질 때
1,1에서 m,n에서 가는 최단 경로의 개수는?
'''
# 풀이 법
'''
미로찾기 BFS알고리즘 사용
기존의 미로찾기 알고리즘을 그대로 쓰면 시간초과가 발생한다.
그러므로 루프를 돌 때의 중복을 최대한 없애줘야한다.

먼저, 아래, 오른쪽만 가는 이상 마지막에 도착하는 것은 무조건 최단거리일 수 밖에없음. 
3x3 맵이 있을 때 문제의 방법으로 대각선으로 가든, 모서리에 붙어서 가든 값이 같음 

만약 3x3 맵이 있을 때
0 0 0
0 0 0
0 0 0
노드를 전부 0으로 초기화 한다.

오른쪽, 아래 루트를 이동한다.
첫 이동때 1 값을 설정해주고 그 값이 이동시마다 옮겨질 수 있도록 한다.(여기서 1은 그 지점 까지의 최단거리의 개수이다.)
만약 오른쪽, 아래를 간다면
0 1 0
1 0 0
0 0 0
이 된다.

이렇게 이동하다보면 서로 경로가 겹칠 때가 있다.
0 1 1
1 1 0
0 0 0
x: 1 y:0에서 아래로 이동후
x: 0 y:1에서 오른쪽으로 이동하면 겹친다.
이 경우 x:0,y:1의 값을 더해주고.
이 때는 queue에 추가하지 않아 루프 도는 횟수를 줄여준다.
이 때에 class를 써서 이미 queue에 들어있는 값도 최신화가 될 수 있도록 한다.

0 1 1
1 2 0
0 0 0

그 이후에도 같은 일이 발생하면 똑같이 한다.
0 1 1
1 2 3
1 0 0

0 1 1
1 2 3
1 3 0

최종적으로 목적지 주변에 3, 3이 있는데 이 값을 더해서 출력하면 된다.
'''


class Obj:
    def __init__(self, a):
        self.value = a

    def sum(self, a):
        self.value += a


def solution(w, h, puddles):
    nodes = [[Obj(0) for _ in range(w)] for _ in range(h)]
    for x, y in puddles:
        nodes[y-1][x-1] = Obj(-1)

    queue = [[0, 0, Obj(1)]]
    while queue:
        y, x, souls = queue.pop(0)
        if y >= 0 and y < h and x >= 0 and x < w:
            if nodes[y][x].value != -1:
                # 이미 방문했다면
                if nodes[y][x].value > 0:
                    # 영혼만 보낸다.
                    nodes[y][x].sum(souls.value)
                else:
                    nodes[y][x].value = souls.value
                    queue.append([y, x+1, nodes[y][x]])
                    queue.append([y+1, x, nodes[y][x]])

    ans = 0
    if nodes[h-2][w-1].value != -1:
        ans += nodes[h-2][w-1].value
    if nodes[h-1][w-2].value != -1:
        ans += nodes[h-1][w-2].value
    return ans % 1000000007


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
