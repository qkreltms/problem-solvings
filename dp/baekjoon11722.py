# https://www.acmicpc.net/problem/11722
n = int(input())
A = list(map(int, input().split()))
d = [0] * (n + 1)
for i in range(n):
    d[i] = 1
    for j in range(i):
        if A[i] < A[j]:
            d[i] = max(d[i], d[j]+1)
print(max(d))