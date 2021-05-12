def f(s):
    stack=[]
    for c in s:
        if c==')':
            x=0
            if not stack:
                return 0
            while stack:
                top=stack.pop()
                if top=='(':
                    if x:
                        stack.append(x*2)
                    else:
                        stack.append(2)
                    break
                elif top=='[':
                    return 0
                else:
                    x+=top
        elif c==']':
            x=0
            if not stack:
                return 0
            while stack:
                top=stack.pop()
                if top=='[':
                    if x:
                        stack.append(x*3)
                    else:
                        stack.append(3)
                    break
                elif top=='(':
                    return 0
                else:
                    x+=top
        else:
            stack.append(c)
    ans=0
    for c in stack:
        if c=='(' or c==')' or c=='[' or c==']':
            return 0
        ans+=c
    return ans
s=input()
print(f(s))
