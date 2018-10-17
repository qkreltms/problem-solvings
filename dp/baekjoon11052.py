n = int(input())
p = list(map(int, input().split()))
d = [0] * (n + 1)
print(p[0])  # p가 1부터 시작하므로 0번째에 0을 넣어줌
p.insert(0, 0)
for i in range(1, n+1):
    for j in range(1, i+1):
        d[i] = max(d[i], d[i-j] + p[j])
print(d[i])
