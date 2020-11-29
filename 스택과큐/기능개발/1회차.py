# 문제
'''
먼저 배포되어야 하는 순서대로 작업의 
진도(A)가 적힌 정수 배열 progresses와
각 작업의 개발 속도가 적힌 정수 배열 speeds가
주어질 때 각 배포마다 몇 개의 기능이 
배포되는지를 return 

배포는 하루에 한 번만 가능하나 
작업은 A순으로 진행하되, 한번에 여러개가 가능하다
단, n번째보다 n+1, n+2,...,n+n 번째가 빨리되면
같은 날에 배포한다.
'''
# 내 실수
'''
'''
# 키포인트
'''
A를 순회하며 남은 날을 구한다.(B)
B를 순회하며 젤 앞의 값을 피봇으로 정하고
그것보다 작은 값을 더해서 정답에 넣어준다.
그 과정에서 A를 앞에서부터 하나씩 지운다.
'''




from math import ceil
from collections import deque
def solution(progresses, speeds):
    remainingDays = deque()
    for (p, s) in zip(progresses, speeds):
        remainingP = 100 - p
        remainingS = remainingP / s
        remainingDays.append(ceil(remainingS))

    ans = []
    while remainingDays:
        pivot = remainingDays.popleft()
        cnt = 1
        for _ in range(len(remainingDays)):
            target = remainingDays[0]
            # 바로 다음 값이 현재의 남은 날 보다 작은지 확인한다.
            if pivot >= target:
                cnt += 1
                remainingDays.popleft()
            # 작지 않으면 바로 끝
            else:
                break
        ans.append(cnt)
    return ans


print(solution([93, 30, 55], [1, 30, 5]), [2, 1])
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]), [1, 3, 2])
