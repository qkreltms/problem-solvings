# 배운 것
'''
heap은 soft한 정렬이라서 중복된 우선순위가 있을 때 어떤 숫자가 먼저 나올지 알기 어려움
즉, [1,1,9,1,1,1], 0의 경우 예상치 못 한 값이 나옴

map의 첫 번째 인자에 lambda를 넣을 수 있다
'''
def solution(ps, l):
    for i, p in enumerate(ps):
        ps[i] = (p, i)
    t = 0
    while ps:
        t += 1 
        p, pi = max(ps, key=lambda x: x[0])
        i = list(map(lambda x: x[0], ps)).index(p)
        ps = ps[i:] + ps[:i]
        ps.pop(0)
        if pi == l:
            return t

print(solution([2, 1, 3, 2], 2), 1)
print(solution([1, 1, 9, 1, 1, 1], 0), 5)
