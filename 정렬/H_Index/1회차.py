# 문제
'''
'''
# 키 포인트
'''

'''
# 풀이
'''
#1
1. 모든 조합을 비교
2. 작은 값이 대체로 결과 값이 됨 => 오름차순 정렬
3. 0~n 번째 순으로 pick하고 배열을 돌면서 
이상 개수 구하고 pick 한 숫자와 값이 같으면 return
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
