def solution(n,number):
    if n == number:
        return 1
    h=[set() for _ in range(8)]
    for i in range(8):
        h[i].add(int(str(n)*(i+1)))
    for i in range(1,8):
        for j in range(i):
            for k in h[j]:
                for l in h[i-j-1]:
                    h[i].add(k+l)
                    h[i].add(k-l)
                    h[i].add(k*l)
                    if l!=0:
                        h[i].add(int(k/l))
        if number in h[i]:
            return i+1
    return -1
                            