def f(N, number):
    if N==number:
        return 1
    S=[set() for _ in range(8)]
    for i in range(1,9):
        S[i-1].add(int(str(N)*i))
    for i in range(1,8):
        for j in range(i):
            for k in S[i-1-j]:
                for l in S[j]:
                    S[i].add(k+l)
                    S[i].add(k-l)
                    S[i].add(k*l)
                    if l != 0:
                        S[i].add(int(k/l))
        if number in S[i]:
            return i+1
    return -1
def solution(N, number):
    return f(N, number)
    