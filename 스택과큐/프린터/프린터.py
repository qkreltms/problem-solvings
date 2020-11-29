# 문제
'''
return 요청한 문서(처음 넣은 배열에서 index 값)가 정렬된 대기열에서 몇 번째 인쇄되는지

인쇄 요청 순으로 인쇄한다.
그 대기열에서 아이템 J를 하나 꺼낸 뒤
중요도가 높은 문서가 대기열에 존재하는지 확인한다.
있다면 J를 대기열 가장 마지막에 넣는다.
없다면 J인쇄
'''
# 내 실수
'''
결과값을 잘 못 이해해서 시간이 좀 소요됨
'''
# 키 포인트
'''
return 값이 index이므로 중요도랑 index를 string으로 묶어준다.
'''
# 알게된 것
'''
deque는 배열 slice가 안됨 (from itertools import islice 사용)
'''




from collections import deque
from itertools import islice
def solution(ps, l):
    q = deque()
    for i, p in enumerate(ps):
        q.append(f'{i} {p}')
    sortedPs = []
    for i in range(len(q)):
        # 중요도가 가장 높은 값을 찾는다.
        m = max(q, key=lambda x: int(x.split()[1]))
        mi = q.index(m)
        # 찾으면 그 값 앞의 배열을 통째로 뒤로 옮긴다.
        q = deque(list(islice(q, mi, len(q))) + list(islice(q, mi)))
        # 중요도 가장 높은 값을 제거한다.
        sortedPs.append(q.popleft())
    for i, p in enumerate(sortedPs):
        # 정렬된 대기열의 index값과 원본 대기열의 index 값(l)이 같은 값을 찾는다.
        if l == int(p.split()[0]):
            # 정렬된 대기열의 index값을 반환한다.
            return i+1


print(solution([2, 1, 3, 2], 2), 1)
print(solution([1, 1, 9, 1, 1, 1], 0), 5)
