'''
'''
# 배운 점
'''
floor가 올림인줄 알고 헤매고 있을 때 끈기있게 질문을 반복해서
읽으며 조건이 다른게 있는지 검토해봤다. 그 결과
"
배포는 하루에 한 번만 할 수 있으며, 
하루의 끝에 이루어진다고 가정합니다. 
예를 들어 진도율이 95%인 작업의 개발 
속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
"
지문을 다시 검토해 봤으며 floor가 아닌 ceil을 써야한다는 결론에
이르렀다.
'''
from math import ceil


def solution(progresses, speeds):
    workingDays = []
    for p, s in zip(progresses, speeds):
        workingDays.append(ceil((100 - p) / s))
    ans = []
    cnt = 0
    pick = workingDays[0]
    for w in workingDays:
        if pick >= w:
            cnt += 1
        else:
            ans.append(cnt)
            pick = w
            cnt = 1
    ans.append(cnt)
    return ans


# print(solution([10, 20, 30, 40], [1, 2, 3, 4]))
print(solution([99, 95], [1,4]))
