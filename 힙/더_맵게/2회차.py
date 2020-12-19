# 풀이법
'''
heap을 2번 팝하고 계산식에 적용
계산식에 적용하기전 가장낮은값이 K이상인지 판별 이상이라면 횟수 반환
만약 scovs가 다 비면 -1 반환
'''
import heapq


def solution(scovs, k):
    heapq.heapify(scovs)
    ans = 0
    while len(scovs) >= 2:
        a = heapq.heappop(scovs)
        b = heapq.heappop(scovs)
        if a >= k:
            return ans
        scov = a+b*2
        ans += 1
        heapq.heappush(scovs, scov)

    if scovs[0] >= k:
        return ans
    return -1


print(solution([1, 1, 1], 4), 2)
print(solution([10, 10, 10, 10, 10], 100), 4)
print(solution([1, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 0, 3, 9, 10, 12], 7), 3)
print(solution([0, 0, 0, 0], 7), -1)
print(solution([0, 0, 3, 9, 10, 12], 7000), -1)
print(solution([0, 0, 3, 9, 10, 12], 0), 0)
print(solution([0, 0, 3, 9, 10, 12], 1), 2)
print(solution([0, 0], 0), 0)
print(solution([0, 0], 1), -1)
print(solution([1, 0], 1), 1)
