# 문제
'''
각각의 숫자가 주어졌을 때 이 숫자를 조합에서
몇 개의 소수를 얻을 수 있는가?
단, 11 == 011
'''
# 풀이법
'''
숫자가 주어지면 그 숫자로 모든 조합을 만들고
그 조합을 순회하면서 숫자로 만들고 소수면
비어있는 dic에 저장해 놓고 비어있지 않으면 카운트 하지 않는다.
'''



from math import sqrt
from itertools import permutations
def isSosu(n):
    if n <= 1:
        return False
    # 2부터 N-1의 수로 나눠서 나눠지는 수가 있으면 반복문 종료
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    allPermutations = []
    ns = list(map(int, numbers))
    for i in range(1, len(ns)+1):
        allPermutations += (list(permutations(ns, i)))
    dic = {}
    ans = 0
    for i in allPermutations:
        n = int(''.join(map(str, i)))
        # 2부터 가장 큰 값까지 돌면서 소수가 아닌 값 제거하면 더 빠를 듯?
        if isSosu(n):
            if n not in dic:
                dic[n]=n
                ans += 1
    return ans


print(solution("17"), 3)
print(solution("011"), 2)
print(solution("111"), 1)
print(solution("999"), 0)
