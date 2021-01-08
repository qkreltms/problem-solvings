'''
'''


class UnionFind:
    def __init__(self, nodeNum):
        self.root = {}
        for i in range(nodeNum):
            self.root[i] = i

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        if y > x:
            self.root[y] = x
        else:
            self.root[x] = y


def kruskal(nodeNum, data):
    weight = 0
    paths = []
    unionFind = UnionFind(nodeNum)
    for d in sorted(data, key=lambda k: k[2]):
        x = unionFind.find(d[0])
        y = unionFind.find(d[1])
        if x is not y:
            unionFind.union(x, y)
            paths.append([d[0], d[1]])
            weight += d[2]
    return paths, weight


print(kruskal(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1],
                  [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]), ([[1, 4, 1], [0, 3, 2], [1, 2, 2], [0, 4, 3], [2, 5, 3]], 11))
