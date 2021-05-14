# 링크: https://velog.io/@deserve82/%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9-%EB%B0%B1%EC%A4%80-%EA%B0%80%EB%A5%B4%EC%B9%A8-%EB%AC%B8%EC%A0%9C%EC%97%90-%EB%8C%80%ED%95%9C-%EA%B3%A0%EC%B0%B0-python
# 매우 스마트하게 알고리즘을 짬 비트마스크 + 'antic' 반복 최적화, 배울만함
import sys


def checker(val):
    cnt = 0
    for word in words:
        if word & val == word:
            cnt += 1
    return cnt


def bf(idx, k):
    global bit, answer
    if k == K:
        answer = max(answer, checker(bit))
        return

    for i in range(idx, 21):
        if not bit & (1 << i):
            # bit를 방문 체크한다. 
            bit |= (1 << i)
            bf(i+1, k+1)
            # 방문 해제한다.
            bit &= ~(1 << i)
    return


N, K = map(int, sys.stdin.readline().split())
words = []
alpha_checker = [False] * len('bdefghjklmopqrsuvwxyz')
alpha_num = {}
for i, a in enumerate('bdefghjklmopqrsuvwxyz'):
    alpha_num[a] = i
for _ in range(N):
    tmp = sys.stdin.readline().rstrip()[4:-4]
    w = 0
    for t in tmp:
        # t가 'antic' 중 하나에 해당하면
        # 걍 이전 값을 그냥 쓰고 loop횟수를 줄인다.
        if t not in 'antic':
            w |= (1 << alpha_num[t])
    words.append(w)
bit = 0
answer = 0
if K < 5:
    print(0)
else:
    K -= 5
    bf(0, 0)
    print(answer)