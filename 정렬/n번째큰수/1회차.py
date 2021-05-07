def f(A):
    A.sort()
    return A[len(A)-3]
t = int(input())
for _ in range(t):
    A = list(map(int, input().split(' ')))
    print(f(A))