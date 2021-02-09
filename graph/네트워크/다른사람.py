'''
computers값을 그대로 사용함
'''
def visit(k, graph, visited):
    visited[k] = 1
    for i in range(len(graph[k])):
        if visited[i] == 0 and graph[k][i] == 1:
            visit(i, graph, visited)

def solution(n, computers):

    visited = [0] * n

    answer = 0

    for i in range(n):
        if visited[i] == 0:
            visit(i, computers, visited)
            answer += 1
        if 0 not in visited:
            break

    return answer