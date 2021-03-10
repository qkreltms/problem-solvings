# 문제
'''
1, ..., n개의 노드가 있을 때 
1번 노드에서 최단경로로 이동시 간선의 개수가 가장 많은(가장 멀리 떨어진)
노드의 개수는? 
'''

# 풀이법
'''
처음에 
    for key, value in edge:
        if key in dic:
            dic[key].append(value)
        else:
            dic[key] = [value]
와 같이 담았을 때 
1-2, 3-1 과 같은 입력일 때 3은 영영 담기지 않는다.
결국 양 노드에 값을 똑같이 줌으로 해결
* 1-2, 1-3 과 같이 root-child로 들어오는 순이아니라면 양 노드에 담아주어야 한다.

    for v in reversed(visited):
        if v != m:
            return cnt
와 같이 구현했을 때
항상 마지막에 위치한 값만 max가 되지 않기 때문에 실패
'''



def solution(n, edge):
    visited = [False for _ in range(n+1)]
    dic = [[] for _ in range(n+1)]
    for a, b in edge:
      dic[a].append(b)
      dic[b].append(a)

    queue = [[1, 1]]
    while queue:
        q, level = queue.pop(0)
        if visited[q] == False:
            visited[q] = level
            for n in dic[q]:
                queue.append([n, level+1])
    m = max(visited)
    cnt = 0
    for v in visited:
        if v == m:
            cnt += 1
    return cnt


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)
print(solution(11, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [
      3, 6], [4, 8], [4, 9], [5, 9], [5, 10], [6, 10], [6, 11]]), 4)
print(solution(4, [[1, 2], [2, 3], [3, 4]]), 1)
print(solution(2, [[1, 2]]), 1)
print(solution(5, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 2)
print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]), 1)
print(solution(4, [[1, 4], [1, 3], [2, 3], [2, 1]]), 3)
print(solution(4, [[3, 4], [1, 3], [2, 3], [2, 1]]), 1)
print(solution(4, [[4, 3], [1, 3], [2, 3]]), 2)
