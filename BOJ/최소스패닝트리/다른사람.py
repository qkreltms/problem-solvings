# 키포인트
'''
find (트리 레벨 최적화), rank, 엣지가 V-1개 일때만 루프돌림
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
# find root node
def find(x):
    if parent[x] < 0:
        return x
    p = find(parent[x])
    parent[x] = p
    return p
# merge two tree
def union(x,y):
    x = find(x)
    y = find(y)

    if x == y: return False

    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y
    return True
# find mst (minimum spanning tree)
def kruskal(n,edges):
    mst = []
    edges.sort() 
    for edge in edges:
        w,x,y = edge
        if union(x,y): 
            mst.append(w) # 가중치만 append
        if len(mst) == n-1: 
            break

    return mst 

# main
N,M = map(int,input().split()) # node, edge
parent = [-1 for _ in range(N+1)]
edges = []
for _ in range(M):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
print(sum(kruskal(N,edges))) # mst의 가중치 출력