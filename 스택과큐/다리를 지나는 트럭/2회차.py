'''
소요시간: 1시간
'''


def solution(bridgeLength, bridgeMaxWeight, truckWeights):
    time = 0
    bridge = []
    sumOfWeigths = 0
    while truckWeights or bridge:
        if time >= bridgeLength:
            sumOfWeigths -= bridge.pop(0)
        if truckWeights:
            truckWeight = truckWeights[0]
            if truckWeight + sumOfWeigths <= bridgeMaxWeight:
                sumOfWeigths += truckWeights.pop(0)
                bridge.append(truckWeight)
            else:
                bridge.append(0)

        time += 1
    return time


print(solution(2, 10, [7, 4, 5, 6]), 8)
print(solution(100, 100, [10]), 101)
print(solution(100, 100, [10 for _ in range(10)]), 110)
print(solution(10000, 10000, [10 for _ in range(10)]), 110)
