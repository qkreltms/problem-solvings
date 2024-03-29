# 링크
'''
문제: https://www.acmicpc.net/problem/1062
'''
# 풀이 법
'''
a~z까지의 k개의 조합안에서 글자를 익혔을 때 최대 단어 읽음 횟수를 출력한다.
a-b-c-d,...
a-b-d-e,...
a-b-f-g,...
a-c-d-e,...
단, a-c-b,...와 같은 조합은 이미 앞에서 했으므로 필요없다.
위의 조합을 만들기 재귀적으로 순회하고 바로위의 조건을 만족시키기 위해 백트레킹 기법을 사용한다.

'''
# 키포인트
'''
문제를 자의로 해석하지말자
N개의 단어와 k개의 "글자"가 있을 때 "최대" 몇 개의 단어를 읽을 수 있을까?
k개의 글자는 a,b,c,d,....를 말함

시간 초과
비트마스크를 쓰지 않으면 k개의 글자로 단어를 읽을 때 n^2의 소요시간이 걸림
사용하면 n 만에 가능 

a-z에서 antic을 제거해 bdefghjklmopqrsuvwxyz 만드는 과정이 오래걸림 추후에는 a-z써놓고 소거하는 식으로 할 것
또는 from string import ascii_lowercase 써서 만들기 
'''


def g():
    cnt = 0
    global words, visited
    for word in words:
        # 단순 비트비교
        if (visited & word) == word:
            cnt += 1
    return cnt


def f(ai, cnt):
    global ans, k, visited
    if cnt == k:
        ans = max(ans, g())
        return
    for i in range(ai, 21):
        if not visited & (1 << i):
            visited |= (1 << i)
            f(i, cnt+1)
            # 백트레킹
            # 이전 방문 비트를 다시 원복함
            visited &= ~(1 << i)


n, k = list(map(int, input().split(' ')))
words = []
h = {}
for i, c in enumerate('bdefghjklmopqrsuvwxyz'):
    h[c] = i
ans = 0
visited = 0
for _ in range(n):
    s = input()[4:-4]
    word = 0
    for c in s:
        # 최적화, 반복문 5회 감소가능
        if c not in 'antic':
            word |= (1 << h[c])
    words.append(word)

if k == 26:
    print(n)
    exit(0)
k -= 5
if k < 0:
    print(0)
    exit(0)
f(0, 0)
print(ans)
