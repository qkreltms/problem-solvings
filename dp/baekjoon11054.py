#https://www.acmicpc.net/problem/11053
n = int(input())
A = list(map(int, input().split()))
d = [0] * n
d2 = [0] * n
for i in range(n):
    d[i] = 1
    for j in range(i):
        if A[i] > A[j]:
            d[i] = max(d[i], d[j]+1)

# D = max(d)
# b = d.index(D)
# for i in range(b, n):
#     d2[i] = 1
#     for j in range(i):
#         if A[i] < A[j]:
#             d2[i] = max(d2[i], d2[j]+1)
#
# D2 = max(d2)
# ans2 = D + D2 - 1
# print(ans2)

d2 = [0] * n
for i in range(n-1, -1, -1):
    d2[i] = 1
    for j in range(n-1, i, -1):
        if A[i] > A[j]:
            d2[i] = max(d2[i], d2[j]+1)

ans = d[0]+d2[0]-1
for i in range(n):
    if ans < d[i]+d2[i]-1:
        ans = d[i]+d2[i]-1
print(ans)






