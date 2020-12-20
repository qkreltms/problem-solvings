# 내 실수
'''
이 부분이 틀림
t += j[0] + j[1]
t는 현재 시간인데 이전 값을 더하면 오류임
'''
import heapq


def solution(jobs):
    jobs.sort()
    t = 0
    heap = []
    cnt = 0
    ans = 0
    while jobs or heap:
        if not heap:
            j = jobs.pop(0)
            t = j[0] + j[1]
            ans += j[1]
        else:
            j = heapq.heappop(heap)
            t += j[0]
            ans += t - j[1]
        cnt += 1

        while jobs and jobs[0][0] <= t:
            j = jobs.pop(0)
            heapq.heappush(heap, (j[1], j[0]))
    return ans // cnt


print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
print(solution([[0, 3], [1, 9], [2, 6]]), 9)
print(solution([[0, 1]]), 1)
print(solution([[1000, 1000]]), 1000)
print(solution([[0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [1000, 1000]]), 500)
print(solution([[100, 100], [1000, 1000]]), 500)
print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)
