'''
트럭 여러 대가 순차적으로 강을 건넌다.
모든 트럭이 건너려면 최소 몇 초?

트럭은 1초에 1만큼 움직임 트럭이 못 가는 경우는 없음

'''


def solution(bridgeLength, bridgeMaxWeight, truckWeights):
    time = 1
    queue = []
    while truckWeights or queue:
        if truckWeights:
            if truckWeights[0] + sum(queue) <= bridgeMaxWeight:
                queue.append(truckWeights.pop(0))
            else:
                queue.append(0)
        time += 1
        if time > bridgeLength:
            queue.pop(0)
    return time


print(solution(2, 10, [7, 4, 5, 6]), 8)
print(solution(100, 100, [10]), 101)
print(solution(100, 100, [10 for _ in range(10)]), 110)
print(solution(10000, 10000, [10 for _ in range(10)]), 10010)
