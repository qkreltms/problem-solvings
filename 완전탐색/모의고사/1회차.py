# 문제
'''
1번 수포자: [1,2,3,4,5, ...]
2번 수포자: [2,1,2,3,2,4,2,5, ...]
3번 수포자: [3,3,1,1,2,2,4,4,5,5, ...]
return 일 때 정답 배열이 주어진다면 가장 높은 점수를 맞을 사람은
누구인가?
단, 높은 점수가 여러일경우, return 하는 값을 오름차순 출력
'''


def solution(ansList):
    supo1 = [1, 2, 3, 4, 5]
    for _ in range(len(ansList) // 5):
        supo1 += [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    for _ in range(len(ansList) // 8):
        supo2 += [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for _ in range(len(ansList) // 10):
        supo3 += [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i, d in enumerate(ansList):
        cnt1 += 1 if supo1[i] == d else 0
        cnt2 += 1 if supo2[i] == d else 0
        cnt3 += 1 if supo3[i] == d else 0
    maxD = max([(cnt1, 1), (cnt2, 2), (cnt3, 3)], key=lambda x: x[0])
    return list(map(lambda x: x[1], list(filter(lambda x: x[0] == maxD[0], [(cnt1, 1), (cnt2, 2), (cnt3, 3)]))))


print(solution([1, 2, 3, 4, 5]), [1])
print(solution([1, 3, 2, 4, 2]), [1, 2, 3])
