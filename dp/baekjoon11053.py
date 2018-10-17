#https://www.acmicpc.net/problem/11053
n = int(input())
A = list(map(int, input().split()))
d = [0] * (n + 1)
for i in range(n):
    d[i] = 1
    for j in range(i):
        if A[i] > A[j]:
            d[i] = max(d[i], d[j]+1)
print(max(d)) #10 20 10 일 때 1이 나오므로 가장 최대값을 출력해줌