# 풀이법
'''
node의 개수만큼의 공간 d를 0으로 만든다.
간선을 받는다. a, b, d[b]+=1
d[i]가 0인 값을 queue에 넣는다.
q가 빌 때까지 순회한다.
q의 젤 아래를 c를 꺼낸다.
그 값을 위상배열에 담는다.
c를 순회하며 이것이 가리키는 노드의 엣지가 있다면 그
가리키는 노드의 d[target]-=1 한다.
d[target] == 0 이라면 target을 queue에 담는다.
queue순회가 종료되면 위상배열을 출력한다.
'''
# 키포인트
'''
그래프의 위상(어떤 노드에 들어오는 간선이 없는 것에서 있는 것으로 순으로)
을 배열에 기록한다.
'''
n, e = map(int, input().split())
d = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    d[b] += 1


def f():
    res = []
    q = []
    for i in range(1, n+1):
        if d[i] == 0:
            q.append(i)
    while q:
        target = q.pop(0)
        res.append(target)
        for g in graph[target]:
            d[g] -= 1
            if d[g] == 0:
                q.append(g)
    return res


print(*f())
'''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

ans
1 2 5 3 6 4 7
'''
