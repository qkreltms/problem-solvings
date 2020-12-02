# 문제(DP 익히면 다시 해볼 것!)
'''
return 평균을 최대한 줄인 순서대(낮은 작업시간을 젤 빨리 처리함)로
하면 시간소요가 어느정도인지

한번에 하나의 작업
요청이 들어온 순대로 단, 정렬 가능
요청 시간이 있음 예를 들어 3ms 시작 작업을 가장 요청시간이 작다는 이유로 
0ms부터 시작 할 수 없음
'''
# 키포인트
'''
1. 이 말의 뜻을 빨리 이해해야한다.
"하드디스크가 작업을 수행하고 있지 않을 때에는 
먼저 요청이 들어온 작업부터 처리합니다."

2. 시간대가 겹쳐있을 때 시작시간이 가장 빠른 순으로 실행 해야 대기시간을 최소로 줄일수 있음 
이경우 대기시간만 계산함
그렇지 않으면 앞의 작업이 끝날때 까지 기다림 + 대기시간
'''
# 내 실수
'''
1. 입력값을 잘 못 이해함
예: [[0,10],[2,12],[9,19],[15,17]] 일 때 0~10(10칸), 2~12(10칸),..., n~m
범위의 값을 차지한다고 생각함, 2에서 시작해 12 시간이 소요됨이 아니라(즉, 0~10(10칸), 2~12(12칸))
2. 
        if not heap:
            s, pt = progress.pop(0)
            t = s + pt
            ans += t # ans += pt가 맞음, 대기시간을 포함한 실행시간만 저장하므로

'''




import heapq
def solution(progress):
    progress.sort()
    heap = []
    t = 0
    ans = 0
    cnt = 0
    # progress 길이만큼만 실행하고픈데, progress는 계속 줄어드므로
    progressLength = len(progress)
    while cnt < progressLength:
        # 비어있을 경우
        if not heap:
            s, pt = progress.pop(0)
            t = s + pt
            ans += pt
        else:
            pt, s = heapq.heappop(heap)
            # 한번에 pt 값까지 더해주고 s를 빼준다. => pt 더하기를 한번 덜 할 수있음
            t += pt
            ans += abs(t - s)
        # 위의 두 작업중 하나는 무조건 하므로
        cnt += 1
        # 총 작업 시간보다 작은 시작 시간을 갖은 값은 모조리 힙에 넣는다. 
        while progress and progress[0][0] <= t:
            s, pt = progress.pop(0)
            # 실행시간 기준으로 heap에 넣는다
            # 그러므로 실행시간 낮은 값이 무조건 root에 위치함
            heapq.heappush(heap, [pt, s])
    return ans // progressLength


print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
print(solution([[0, 3], [1, 9], [2, 6]]), 9)
print(solution([[0, 1]]), 1)
print(solution([[0, 1], [1000, 1000]]), 1001)
