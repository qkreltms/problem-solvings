# https://www.acmicpc.net/problem/9466
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
# 답은 맞게 나오지만 시간, 메모리 초과가 나온다 => 재귀라서 그렇지 않을까?, => deep copy => 재방문 비허용 방법으로
# 5. 답이 틀리게 나온다 왜?? => 중간지점에 cycle이 있는데 그 cycle이 2개 이상의 노드일 때 반례가있음
# 반례
# 1
# 9
# 8 3 4 5 6 7 4 1 3
# 6. 속도를 줄이자 => node 생성 1차원 배열로 가능함 (하나의 노드가 2개 이상 값을 가질수 없으므로)
import sys

def node(L):
    N = [0] * L
    i = 0
    for n in map(int, sys.stdin.readline().split(" ")):
        i+=1
        N[i] = n
    return N

def f(c):
    global ans
    while True:
        if V[c]:
            if c in track:
                ans += track[track.index(c):]
            break
        track.append(c)
        V[c] = True
        c = N[c]

T = int(sys.stdin.readline())
for _ in range(T):
    L = int(sys.stdin.readline()) + 1
    N = node(L)
    global V 
    V = [False] * L
    ans = []
    track = []

    for i in range(1, L):
        if not V[i]:
            track = [i]
            V[i] = True
            f(N[i])
    print(L - 1 - len(ans))
