def solution(N, number):
    def f():
        A=[set() for _ in range(8)]
        for i in range(8):
            A[i].add(int(str(N)*(i+1)))
        for i in range(1,8):
            for j in range(i):
                for a in A[i-1-j]:
                    for b in A[j]:
                        A[i].add(a+b)
                        A[i].add(a-b)
                        A[i].add(a*b)
                        if b != 0:
                            A[i].add(int(a/b))
            if number in A[i]:
                return i
        return -1
    return f()
print(solution(5,12))
        