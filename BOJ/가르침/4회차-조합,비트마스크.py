# 키 포인트
'''
defference를 사용하면 피연산자가 set이 아닌 list, 문자열, 숫자 등이라도 가능
'''
from itertools import combinations
from string import ascii_lowercase

n, k = list(map(int, input().split(' ')))
words = []
antic = set(['a', 'n', 't', 'i', 'c'])
alphabets = set(ascii_lowercase)-antic
h = {}
for i, c in enumerate(alphabets):
    h[c] = (1 << i)

for _ in range(n):
    word = set(input()[4:-4])-antic
    bit = 0
    for c in word:
        bit |= h[c]
    words.append(bit)
k -= 5
if k < 0:
    print(0)
    exit(0)
if k == 26:
    print(n)
    exit(0)

ans = 0
combsSource = set()
for i in range(21):
    combsSource.add(2**i)
for comb in list(combinations(combsSource, k)):
    cur = sum(comb)
    cnt = 0
    for w in words:
        if (w & cur) == w:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
