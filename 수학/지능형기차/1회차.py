#링크
'''
문제: https://www.acmicpc.net/problem/2460
참고:
'''
#풀이 법
'''
'''
#키포인트
'''
'''

def f():
    m=0
    s=0
    while True:
        a,b = list(map(int, input().split(' ')))
        s+=b-a
        if m < s:
            m = s
        if s == 0:
            break
    return m

print(f())