# 문제
'''
무인도 to 어디론가 구명보트를 이용해 구출하려한다.
단, 최대 2명만 탑승가능, 무게제한 있음

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의
무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만
1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을
초과하여 같이 탈 수 없습니다.

return 구명보트 최소 사용 횟수.
'''
# 키포인트
'''
정렬 후 가장 낮은 값, 가장 큰 값 limit 넘는지 비교하면서 인덱스 사용하면서 배열 서로 좁힘
'''
# 풀이법
'''
1트:
2개짜리 조합을 만들고
그 합이 limit에 가까운 것을 배열에서 제거하면서 카운트한다.

조합만드는 법 =>
min heap, max heap을 만들고
min heap에서 하나 꺼낸 후 max heap에서 하나를 꺼낸다
만약 limit를 넘으면 어딘가에 저장해 놓고 하나 더 꺼낸다. 반복,
만약 max heap에서 limit에 맞는 값을 찾으면 ans +=1 없으면 꺼낸것 다시 저장

시간 초과 발생!
=> heap을 사용하지 말고 sort를 사용하면 더 간단히 할 수 있을 듯?
또 시간 초과 발생! ㅠㅠ
=> 그리디 관점에서 생각해보자... 젤 낮은 값과 모든 값을 더해서 초과하는 값은 제외
시간 초과...
=> 결국은 봤다, 답은 원리는 그리디 관점에서 생각해 본것과 비슷하다, 다만 O(n^2)이 아니라는 것

'''
# 시간
'''
21/01/03/18:42 ~ 22:39 (-2h)
'''

# 1
# import heapq
# def solution(people, limit):
#     minHeap = []
#     maxHeap = []
#     ans = 0
#     for p in people:
#         heapq.heappush(maxHeap, -p)
#         heapq.heappush(minHeap, p)
#     while minHeap:
#         a = heapq.heappop(minHeap)
#         maxHeap.remove(-a)
#         maxHeapTemp = []
#         l = len(maxHeap)
#         b = 0
#         flag = False
#         for i in range(l):
#             b = -heapq.heappop(maxHeap)
#             if limit-a >= b:
#                 flag = True
#                 break
#             maxHeapTemp.append(-b)
#         for t in maxHeapTemp:
#             heapq.heappush(maxHeap, t)
#         if flag:
#             minHeap.remove(b)
#         ans += 1
#     return ans

# 2
# def solution(people, limit):
#     people.sort()
#     ans = 0

#     while people:
#         p = people.pop(0)
#         ei = len(people)-1
#         while ei >= 0:
#             if limit-p >= people[ei]:
#                 people.pop(ei)
#                 break
#             ei -= 1
#         ans += 1
#     return ans
# 3


def solution(people, limit):
    answer = 0
    i, j = 0, len(people)-1
    people.sort(reverse=True)
    while i <= j:
        if people[i] + people[j] <= limit:
            j -= 1
         i += 1
        answer += 1
    return answer


print(solution([70, 50, 80, 50], 100), 3)
print(solution([40, 40, 70, 50, 80, 50], 120), 3)
print(solution([70, 80, 50], 100), 3)
print(solution([40, 40, 40], 160), 2)
print(solution([40], 160), 1)
print(solution([240], 240), 1)
print(solution([40, 50, 60, 240], 240), 3)
