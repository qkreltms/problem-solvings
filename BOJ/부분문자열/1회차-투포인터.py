#링크
'''
문제: https://www.acmicpc.net/problem/16916
'''
#풀이 법
'''
투포인터를 사용한다, 다만 시간초과
'''
#키포인트
'''
'''

s=input()
p=input()
def f():
    l,r=0,0
    while (l+r)<len(s):
        if s[l+r] == p[r]:
            r+=1
            if r == len(p)-1:
                return 1
        else:
            l+=1
            r=0
    return 0
print(f())