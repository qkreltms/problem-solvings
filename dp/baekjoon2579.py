n = int(input())
A = [0]
for i in range(n):
    A.insert(i, int(input()))
A.insert(0, 0)  # A는 1부터 시작

d = [0] * (n + 1)
d[1] = A[1]
if n <= 1:
    print(d[n])
d[2] = A[1] + A[2]
for i in range(n+1):
    d[i] = max(d[i-3] + A[i-1] + A[i], d[i-2] + A[i])
print(d[n])