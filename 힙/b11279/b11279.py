#문제
'''
최대 힙 구현
입력:
첫 줄 = 연산의 개수 => k
두번째 줄 ~ k
0일 경우 루트 출력
n일 경우 값을 최대 힙에 넣음
'''

import sys
import heapq
k = int(sys.stdin.readline())
heap = []
for _ in range(k):
    n = int(sys.stdin.readline())
    if n > 0:
        heapq.heappush(heap, (-n, n))
    if n == 0:
        if len(heap) == 0:
            print(0)
        else: 
            print(heapq.heappop(heap)[1])