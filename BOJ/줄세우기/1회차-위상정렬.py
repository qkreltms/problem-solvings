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