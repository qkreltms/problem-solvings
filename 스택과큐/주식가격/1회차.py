'''
1. 초 단위로 기록된 주식가격이 담긴 배열 prices가 주어진다.
2. 가격이 떨어지지 않은 기간은 몇 초인지 반환하라.
[1,2,3,2,3]일 때
1초 시점의 1$는 배열 끝까지 순회했을 때 떨어진 적이 없다 => 배열 길이 (4)
2초 시점의 2$는 끝까지 떨어지지 않았다. => 자신의 index - 배열 길이 (3)
3초 시점의 3$는 배열 끝까지 순회했을 때 1초뒤 가격이 떨어졌다. => 1
4초 시점의 2$는 배열 끝까지 순회했을 때 1초간 가격이 떨어지지 않았다.
5초 시점의 3$는 배열 끝까지 순회했을 때 0초간 가격이 떨어지지 않았다.

생각 1.
Queue를 써서 앞 배열을 pop한 후 a에 저장, 배열을 순회한다. a > arr[i]일 경우  index값을 반환하고 처음부터 배열이 빌때까지 다시 진행.
다 순회하고도 없으면 index 값 반환 
'''
# 배운 점
'''
현재 알고리즘에서 시간 초과가 난다?
1. 더 빠른 자료구조로 바꿔본다. list에서 deque로 변경
2. 그래도 안되면 알고리즘에서 최적화 할 수 있는 부분 접근
3. 그래도 안되면 다른 방식으로 풀어본다.
'''
# 1회차 클리어
from collections import deque


def solution(prices):
    q = deque(prices)
    ans = []
    for i in range(len(prices)):
        pivot = q.popleft()
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if pivot > prices[j]:
                break

        ans.append(cnt)
    return ans


print(solution([1, 2, 3, 2, 3]), [4, 3, 1, 1, 0])
