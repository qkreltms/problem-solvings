from itertools import combinations

x = []
for i in range(9):
    x.append(int(input()))
for i in combinations(x, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break