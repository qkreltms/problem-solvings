import sys

par=sys.stdin.readline()
stack=[]
pt=[0]
op="[("
cl="])"
ok=True
for c in par:
    if c in op:
        stack.append(c)
        pt.append(0)
    elif c in cl:
        if len(stack)==0:
            ok=not ok
            break
        
        elif c==')' and stack[-1]=='(':
            res=pt.pop()
            pt[-1]+=res*2 if res!=0 else 2
            stack.pop()
            
        elif c==']' and stack[-1]=='[':
            res=pt.pop()
            pt[-1]+=res*3 if res!=0 else 3
            stack.pop()
        else:
            ok=False
            break
    else:
        pass

if ok:
    sys.stdout.write(str(pt[0]))
else:
    print(0)