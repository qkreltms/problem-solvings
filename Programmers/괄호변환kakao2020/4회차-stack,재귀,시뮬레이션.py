from collections import Counter
def solution(p):
    def isCorrect(w):
        stack=[]
        for c in w:
            if c == ')':
                if not stack:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return True
    def isPair(w):
        c=Counter(w)
        if c['('] == c[')']:
            return True
        return False
    def getUV(w):
        x=''
        while w:
            x+=w[:2]
            w=w[2:]
            if isPair(x):
                return (x, w)
        return (x,'')
    def f(w):
        if not w:
            return ''
        u,v=getUV(w)
        if isCorrect(u):
            return f'{u}{f(v)}'
        return f"({f(v)}){''.join(list(map(lambda x: '(' if x == ')' else ')',u[1:-1])))}"
    return f(p)
        