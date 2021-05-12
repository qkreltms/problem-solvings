# 키 포인트
'''
UV를 구하는 방법이 어려울 수도 있는데 예제에 힌트가 있음

2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
예제에서
()))(((), U=(), V=))((() 로 잡혔고
(()())(), U=(()()), V=()로 잡혔으므로 왼쪽에서부터 2칸씩 자르면 된다.

디스트럭팅할 때 주의!!
U,V=['', 1]는 에러 발생
U,V=('', 1)은 정상
'''

from collections import Counter


def solution(P):
    def isCorrect(s):
        while True:
            r = s.find('()')
            if r == -1:
                return False
            elif len(s) <= 2:
                return True
            elif r == 0:
                s = s[r+2:]
            elif r == len(s)-2:
                s = s[:r]
            else:
                s = s[:r]+s[r+2:]

    def isPair(s):
        c = Counter(s)
        if c[')'] == c['(']:
            return True
        return False

    def getUV(s):
        front = ''
        while s:
            front += s[:2]
            rear = s[2:]
            s = rear
            if isPair(front):
                return (front, rear)

    def f(p):
        if not p:
            return ''
        u, v = getUV(p)
        if isCorrect(u):
            return f'{u}{f(v)}'
        u = u[1:len(u)-1]
        tempU = list(u)
        for i, c in enumerate(tempU):
            if c == '(':
                tempU[i] = ')'
            else:
                tempU[i] = '('
        return f'({f(v)}){"".join(tempU)}'
    return f(P)


# print(solution('(())'), '(())')
print(solution('(()())()'), '(()())()')
