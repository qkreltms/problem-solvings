def getUV(s):
    for i in range(2,len(s)+1,2):
        x = s[:i]
        cnt = 0
        for c in x:
            if c == ')':
                cnt+=1
            else:
                cnt-=1
        if cnt == 0:
            return (s[:i],s[i:])
    return (s, '')
    
def isCorrect(s):
    stack=[]
    for c in s:
        if c == '(':
            stack.append('(')
        elif not stack:
            return False
        else:
            stack.pop()
    if stack:
        return False
    return True
        
def f(s):
    if not s:
        return ''
    u,v=getUV(s)
    if isCorrect(u):
        return f'{u}{f(v)}'
    return f'({f(v)}){"".join(list(map(lambda x:"(" if x == ")" else ")" ,u[1:-1])))}'
def solution(P):
    return f(P)

solution("(()())()")