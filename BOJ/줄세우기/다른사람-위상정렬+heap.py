import heapq
import io
import os
import sys
input = input

def topologicalSort():
    n, m = map(int, input().split())
    number = [0 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        number[b] += 1
    que = []
    for i in range(1, n+1):
        if number[i] == 0:
            heapq.heappush(que, i)
    res = []
    for i in range(n):
        tmp = heapq.heappop(que)
        res.append(tmp)
        for p in graph[tmp]:
            number[p] -= 1
            if number[p] == 0:
                heapq.heappush(que, p)
    sys.stdout.write(' '.join(map(str,res)))


if __name__ == '__main__':
    topologicalSort()