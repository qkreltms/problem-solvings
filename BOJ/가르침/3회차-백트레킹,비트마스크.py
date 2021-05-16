def g():
    cnt = 0
    for w in words:
        if (w & visited) == w:
            cnt += 1
    return cnt


def f(si, cnt):
    global ans, visited
    if k == cnt:
        ans = max(ans, g())
        return
    for i in range(si, 21):
        visited |= (1 << i)
        f(i+1, cnt+1)
        visited &= ~(1 << i)


n, k = list(map(int, input().split(' ')))
words, h, ans, visited = [], {}, 0, 0
alphabets = 'bdefghjklmopqrsuvwxyz'
for i, c in enumerate(alphabets):
    h[c] = i
for _ in range(n):
    word = input()[4:-4]
    bit = 0
    for c in word:
        if not c in 'antic':
            bit |= (1 << h[c])
    words.append(bit)
k -= 5
if k < 0:
    print(0)
    exit(0)
if k == 26:
    print(n)
    exit(0)
f(0, 0)
print(ans)
