import heapq


def solution(jobs):
    count, last, answer = 0, -1, 0
    heap = []
    jobs.sort()
    # 시작시간 초기화
    time = jobs[0][0]
    while count < len(jobs):
        for s, t in jobs:
            if last < s <= time:
                # 작업 소요시간으로 min heap을 만들기 위해 (t, s) 푸시
                heapq.heappush(heap, (t, s))
        # 바로 수행할 수 있는 작업이 있는 경우
        if len(heap) > 0:
            count += 1
            last = time
            term, start = heapq.heappop(heap)
            time += term
            answer += (time - start)
        # 바로 수행할 수 있는 작업이 없는 경우
        else:
            time += 1
    return answer//len(jobs)
print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]))

# print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]))
