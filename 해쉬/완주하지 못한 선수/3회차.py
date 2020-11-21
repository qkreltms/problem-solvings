def solution(a, b):
    a.sort()
    b.sort()
    for (i, c) in enumerate(a):
        if i == len(a)-1:
            return a[i]
        if c != b[i]:
            return c
