from sys import stdin
input = stdin.readline

test_nbr = int(input())

def bipartiteCheck():
    v,e = map(int,input().split())

    COLOR = [None for _ in range(v+1)]
    ADJ = [[] for _ in range(v+1)]
    TOVISIT = []
    NODE = set([i for i in range(1,v+1)])

    for i in range(e):
        v1, v2 = map(int, input().split())
        ADJ[v1].append(v2)
        ADJ[v2].append(v1)

    while bool(NODE):
        c = NODE.pop()
        TOVISIT.append(c)
        while TOVISIT != []:
            start = TOVISIT[0]
            for u in ADJ[start]:
                if COLOR[u] is not None:
                    if COLOR[u] is COLOR[start]:
                        return 'NO'
                else:
                    COLOR[u] = not COLOR[start]
                    TOVISIT.append(u)
            del TOVISIT[0]
            if start != c: NODE.remove(start)

    return 'YES'


for _ in range(test_nbr):
    print(bipartiteCheck())