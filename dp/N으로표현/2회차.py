'''
'''


def solution(N, number):
    if N == number:
        return 1
    if int(str(N)*9) == number:
        return 9

    ans = -1
    mySets = [set() for _ in range(9)]
    for i, s in enumerate(mySets, start=1):
        s.add(int(str(N)*i))

    for i in range(1, 8):
        for j in range(i):
            for b in mySets[i-1-j]:
                for a in mySets[j]:
                    mySets[i].add(a+b)
                    mySets[i].add(a-b)
                    mySets[i].add(a*b)
                    if b != 0:
                        mySets[i].add(a//b)
        if number in mySets[i]:
            ans = i+1
            break
    return ans


print(solution(5, 12), 4)
print(solution(2, 11), 3)
print(solution(1, 1121), 7)
print(solution(8, 53), 5)
print(solution(8, 888888888), 9)
