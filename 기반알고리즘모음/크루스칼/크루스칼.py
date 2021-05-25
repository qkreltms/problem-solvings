'''
그래프와 엣지가 주어질 때 전체를 보고 최단 거리를 구한다.
프림 알고리즘은 거처간 노드에서 최단 거리 구함
https://brownbears.tistory.com/396

'''
'''
rank의 목적 자세히 알아보기 =>  
비대칭적 트리가 되었을 때 배열로 순회하는게 더 빠름 rank 사용해 최적화 
https://bowbowbow.tistory.com/26
'''


class DisjointSet:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, v):
        # 자식 노드가 최상위 부모를 가리키도록 높이를 최적화한다.
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, root1, root2):
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1


def kruskal(n, info):
    minimum_weight = 0
    disjointset = DisjointSet(n)
    result = []
    for data in sorted(info, key=lambda cost: cost[2]):
        v, u, _ = data
        root1 = disjointset.find(v)
        root2 = disjointset.find(u)
        if root1 != root2:
            disjointset.union(root1, root2)
            result.append(data)
            minimum_weight += data[2]
    return result, minimum_weight


print(kruskal(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [
      2, 5, 3], [4, 5, 4]]), ([[1, 4, 1], [0, 3, 2], [1, 2, 2], [0, 4, 3], [2, 5, 3]], 11))
