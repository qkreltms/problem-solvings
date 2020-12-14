def solution(ansList):
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnts = [0, 0, 0]
    for i, d in enumerate(ansList):
        cnts[0] += 1 if supo1[i % len(supo1)] == d else 0
        cnts[1] += 1 if supo2[i % len(supo2)] == d else 0
        cnts[2] += 1 if supo3[i % len(supo3)] == d else 0
    maxD = max(cnts)
    ans = []
    for i, d in enumerate(cnts):
        if d == maxD:
            ans.append(i+1)
    return ans


print(solution([1, 2, 3, 4, 5]), [1])
print(solution([1, 3, 2, 4, 2]), [1, 2, 3])
