'''

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
            if pivot >= target:
                cnt += 1
                remainingDays.popleft()
            else:
                break
        ans.append(cnt)
    return ans


print(solution([93, 30, 55], [1, 30, 5]), [2, 1])
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]), [1, 3, 2])

'''
다른 사람 풀이법
'''
def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer