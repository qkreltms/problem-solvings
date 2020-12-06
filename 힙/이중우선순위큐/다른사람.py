
# 배운 것
'''
remove = pop(index(value))

문제에 최소 2개는 남는다는 가정이 있음. (원소는 “명령어 데이터” 형식으로 주어집니다.
- 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다. => 마지막 처리 말하는듯??)
'''
import heapq


def solution(operations):
    heap = []

    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            # D -1일 때
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]


print(solution(["I 7", "I 5", "I -5", "D -1",  "D -1"]), [7, 5])
