from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        # 합집합 연산 참고: https://wikidocs.net/16044
        # 순열을 만들면서 중복이 발생하는데 합집합 연산으로 합침 + 중복제거
        # 애초에 리스트 쓰듯이 += 안됨
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    # 차집합 연산
    # 이전 집합에서 중복을 제외한 집합만 합친다.
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

print(solution("17"), 3)
print(solution("011"), 2)
print(solution("111"), 1)
print(solution("999"), 0)