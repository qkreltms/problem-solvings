# 문제
'''
1, ..., n개의 노드가 있을 때 
1번 노드에서 최단경로로 이동시 간선의 개수가 가장 많은(가장 멀리 떨어진)
노드의 개수는? 
'''


def solution(n, edge):
    visited = [False for _ in range(n+1)]
    for e in edge:
        e.sort()
    dic = {}
    for key, value in edge:
        if key in dic:
            dic[key].append(value)
        else:
            dic[key] = [value]

    queue = [[1, 1]]
    while queue:
        q, level = queue.pop(0)
        if visited[q] == False:
            visited[q] = level
            if q in dic:
                nodes = dic[q]
                for n in nodes:
                    queue.append([n, level+1])
    m = max(visited)
    cnt = 0
    for v in reversed(visited):
        if v != m:
            return cnt
        cnt += 1


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)
print(solution(11, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [
      3, 6], [4, 8], [4, 9], [5, 9], [5, 10], [6, 10], [6, 11]]), 4)
print(solution(4, [[1, 2], [2, 3], [3, 4]]), 1)
print(solution(2, [[1, 2]]), 1)
print(solution(5, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 2)
