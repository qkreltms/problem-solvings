def solution(s):
    ans=1001
    if len(s) == 1:
        return 1
    for i in range(1,len(s)//2+1):
        a,b=0,i
        table=[s[a:b]]
        while b<len(s):
            a=b
            b=b+i
            table.append(s[a:b])
        w,c,l='',1,0
        for token in table:
            if w!=token:
                w=token
                l+=len(w)
                if c>1:
                    l+=len(str(c))
                    c=1
            else:
                c+=1
        if c>1:
            l+=len(str(c))
        ans=min(ans,l)
    return ans
            