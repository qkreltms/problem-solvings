#문제
'''
https://programmers.co.kr/learn/courses/30/lessons/43165
숫자가 배열로 주어질 때 더하고 빼서 target을 만드는 방법의 수를 반환하라
'''
#키포인트
'''
1. 이 문제를 어떻게 dfs로 생각해서 구현하느냐
'''
#풀이법
'''
[1,2,1,2], 2가 주어질 경우 조합은 [-1,2,-1,2], [1,-2,1,2], [1,2,1,-2] 총 3개이다.
배열의 첫번째부터 하나씩 더하거나 빼는 식으로 재귀적으로 순회하며 배열의 끝까지
순회했을 때 정답과 일치하는지 확인한 후 맞다면 1을 반환한다.
'''
#배운 것
'''
문제에는 안나와 있지만 숫자의 순서는 바뀌지 않음 
=> 레벨이 2이하면 포괄적으로 생각하지 말자
'''
def dfs(numbers, target):
    if numbers == []:
        if t == target:
            return 1
        else:
            return 0
    return dfs(numbers[1:], target+numbers[0]) + dfs(numbers[1:], target-numbers[0])

def solution(numbers, target):
    global t
    t = target
    return dfs(numbers, 0)

print(solution([1,2,1,2], 2), 3)
print(solution([1,2,1,2], 6), 1)