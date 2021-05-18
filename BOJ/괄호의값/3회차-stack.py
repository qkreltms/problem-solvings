def f():
    stack=[]
    for c in s:
        if c==')':
            r=0
            if not stack:
                return 0
            while True:
                t=stack.pop()
                if t=='(':
                    if r:
                        stack.append(2*r)
                    else:
                        stack.append(2)
                    break
                elif not stack or t=='[':
                    return 0
                else:
                    r+=t
        elif c==']':
            r=0
            if not stack:
                return 0
            while True:
                t=stack.pop()
                if t=='[':
                    if r:
                        stack.append(3*r)
                    else:
                        stack.append(3)
                    break
                elif not stack or t=='(':
                    return 0
                else:
                    r+=t
        else:
            stack.append(c)
    ans=0
    for c in stack:
        if not isinstance(c, int):
            return 0
        ans+=c
    return ans
s=input()
print(f())