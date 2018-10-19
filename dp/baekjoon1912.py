n = int(input())
A = list(map(int, input().split()))
D = [0] * n
for i in range(n):
    D[i] = A[i]
    if i is 0:
        continue
    D[i] = max(D[i-1]+D[i], A[i])
print(max(D))