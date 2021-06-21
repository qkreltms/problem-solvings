# 키포인트
'''
"()))((()"일 때 u가 오른쪽 부터 잘라서 얻는 줄 알고 헤맸다. 이때의 내 고정관념이
"(()())()"일 때  ()(()())가 되어야 한다고 고집부렸다. 답은 (()())() 인데...

답이 생각했던것과 다르다면 다른 예제를 처음부터 다시 살펴보자.
'''
def getUV(p):
    cnt=0
    i=0
    while i<len(p):
        c=p[i]
        if c==')':
            cnt+=1
        else:
            cnt-=1
        i+=1
        if cnt==0:
            return (p[:i],p[i:])
    return (p,'')
def isCorrect(p):
    stack=[]
    p=list(p)
    while p:
        t=p.pop(0)
        if t == ')':
            if not stack:
                return False
            stack.pop()
        else:
            stack.append(t)
    return True
def solution(p):
    if not p:
        return ''
    u,v=getUV(p)
    if isCorrect(u):
        return f'{u}{solution(v)}'
    return f'({solution(v)}){"".join(list(map(lambda x: "(" if x==")" else ")",u[1:-1])))}'