'''
백트레킹 기법을 사용했지만 1회차에 비해 2배 느림
'''


def solution(numbers, target):
    ans = 0
    queue = [([*numbers], 0), ([-1*numbers[0], *numbers[1:]], 0)]
    while queue:
        qNumbers, i = queue.pop()
        if sum(qNumbers) == target:
            ans += 1
            continue

        if len(numbers) > i+1:
            queue.append(([*qNumbers], i+1))
            qNumbers[i+1] = -1*qNumbers[i+1]
            queue.append(([*qNumbers], i+1))
    return ans


print(solution([1, 1, 1, 1, 1], 3), 5)
print(solution([1, 2, 1, 2], 2), 3)
print(solution([1, 2, 1, 2], 6), 1)
