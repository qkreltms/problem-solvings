import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
from collections import deque

def BOJ1707():    
    def BFS(start):
        queue = deque([start])
        grouped[start] = 1
        while queue:
            curr = queue.popleft()
            # 현재 노드의 색을 가져온다.
            group = grouped[curr]
            # 현재 노드의 인접 리스트를 가져온다.
            for nbhd in G[curr]:
                if grouped[nbhd]:
                    # 그룹이 정해진 노드만 들어온다 0은 들어올 수 없음
                    # 인접 리스트가 그룹(색)이 같으면 이분 그래프가 아니다.
                    if grouped[nbhd] == group:
                        return False
                    # 그룹이 다르면
                    continue
                # 현재 그룹에서 반대 그룹으로 해줌
                grouped[nbhd] = -group
                queue.append(nbhd)
        return True

    k = int(input())
    for _ in range(k):
        v,e = map(int, input().split())
        G = {i:[] for i in range(1,v+1)}
        for _ in range(e):
            i,j = map(int,input().split())
            G[i].append(j)
            G[j].append(i)

        grouped = [0]*(v+1)
        for start in range(1,v+1):
            if not grouped[start]:
                if not BFS(start):
                    print("NO")
                    break
        else:
            print("YES")
BOJ1707()