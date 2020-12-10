# 문제
'''
return h-index
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 
논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 
h의 최댓값이 이 과학자의 H-Index입니다.

과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
'''
# 키 포인트
'''
1. h가 작은 값이 대체로 결과 값이 됨 => 오름차순 정렬
'''
# 풀이
'''
#1
1. 모든 조합을 비교
2. h가 작은 값이 대체로 결과 값이 됨 => 오름차순 정렬
3. 0~n 번째 순으로 돌면서 N 값 하나 pick하고 배열을 돌면서 
이상 개수 구하고 가장 이상 개수가 많은 n번째 숫자 출력
'''


def solution(N):
    N.sort()
    l = len(N)
    cnts = []
    for pick in range(l+1):
        cnt = 0
        for j in N:
            if pick <= j:
                cnt += 1
        if pick > cnt:
            break
        cnts.append((pick, cnt))
    return max(cnts, key=lambda x:x[0])[0]


print(solution([3, 0, 6, 1, 5]), 3)
print(solution([0, 0, 0, 0, 0]), 0)
print(solution([0, 0, 0, 0, 2, 3]), 2)
print(solution([0, 0, 0, 3, 5, 5, 6, 7, 7, 8]), 5)
print(solution([350, 452, 877]), 3)
