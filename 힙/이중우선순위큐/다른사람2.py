'''
가정:min heap에서 pop한 아이템이 max heap의 루트보다 크다면 
모든 이중우선순위큐를 다 돌았다.
'''
from heapq import heappush, heappop

def solution(arguments):
    max_heap = []
    min_heap = []
    for arg in arguments:
        if arg == "D 1":
            if max_heap != []:
                heappop(max_heap)
                if max_heap == [] or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
        elif arg == "D -1":
            if min_heap != []:
                heappop(min_heap)
                if min_heap == [] or -max_heap[0] < min_heap[0]:
                    max_heap = []
                    min_heap = []
        else:
            num = int(arg[2:])
            heappush(max_heap, -num)
            heappush(min_heap, num)
    if min_heap == []:
        return [0, 0]
    return [-heappop(max_heap), heappop(min_heap)]