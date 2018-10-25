n, k = list(map(int, input().split()))
yak = [0]
for i in range(1, int((n * 0.5))+1):
    if n % i is 0:
        yak.append(i)
yak.append(n)
if len(yak)-1 < k:
    print(0)
else:
    print(yak[k])
print(yak)