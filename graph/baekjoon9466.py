# 사이클 탐지 문제, but 사이클 탐지 되지 않는 집합의 개수를 말하라
# 1. 첫번째 생각: 
# 시작 노드를 재방문 할경우 사이클이 있다! 
# But 시작 노드가 사이클의 시작점이 아닐 수 있다.
# 2. 두번째 생각
# 어떤 노드를 재방문 했을 때 사이클이 있다!
# 사이클을 탐지 할 수있지만 어떤 집합의 사이클인지 알 수 없다.
# 3. 세번째 생각
# 유방향, 재방문허용, n번까지 루프, 자기자신 발견시 사이클, 사이클 발견시 해당 노드 특정 사인 부여 후 나중에 그 사인 카운트
# 4. 네번째 생각
# 답은 맞게 나오지만 시간, 메모리 초과가 나온다 => 재귀라서 그렇지 않을까?

import copy
import sys
sys.setrecursionlimit(999999)

def node(L):
    res = [[] for i in range(L)]
    for i, n in enumerate(map(int, sys.stdin.readline().split(" "))):
        res[i + 1].append(n)
    return res

def f(root, C, V):
    c = C.pop()
    if c == root:
        V[root] = 2
        return
    if c in track:
        V[c] = 2
        return
    
    track.append(c)
    f(root, copy.deepcopy(N[c]), V)

T = int(sys.stdin.readline())
for _ in range(T):
    L = int(sys.stdin.readline()) + 1
    N = node(L)
    V = [0] * L
    track = [0] * L

    for n in range(1, L):
        track = []
        f(n, copy.deepcopy(N[n]), V)

    res = L - 1
    for i in V:
        if i == 2:
            res -= 1
    print(res)