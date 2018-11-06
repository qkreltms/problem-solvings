# https://www.acmicpc.net/problem/2670
n = int(input())
A = [0]
for i in range(n):
    A.append(float(input()))
A.remove(0)
D = [0] * n
D[0] = A[0]
for i in range(1, n):
    D[i] = A[i]
    D[i] = max(D[i-1]*D[i], A[i])
print("{0:.3f}".format(round(max(D), 3)))
