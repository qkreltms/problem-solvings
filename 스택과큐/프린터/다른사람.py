#키포인트
'''
1. 나는 string으로 i,p를 묶었는데 여기선 tuple로 묶는다.
2. any(), any의 파라메터중 하나라도 참인 값이 있으면 그 값을 반환
'''
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        # 하나 씩 정렬을 진행한다.
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        # 정렬이 다 끝나면 들어온다.
        else:
            # 앞에서부터 하나씩 제거하면서 값을 찾는다.
            answer += 1
            if cur[0] == location:
                return answer

print(solution([2, 1, 3, 2], 2), 1)
print(solution([1, 1, 9, 1, 1, 1], 0), 5)