import sys

sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def dfs(graph: list, node: int, visited: list, line: list):
    if visited[node]:
        return
    visited[node] = True

    for child in graph[node]:
        dfs(graph, child, visited, line)
    
    line.append(node)
    


def solution(n: int, m: int, g: list):
    visited = [False for _ in range(n+1)]
    line = []
    for node in range(1, n+1):
        if not visited[node]:
            dfs(g, node, visited, line)

    return ' '.join(map(str, reversed(line)))


def main():
    n, m = read_list_int()
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = read_list_int()
        g[a].append(b)
    print(solution(n, m , g))


if __name__ == '__main__':
    main()