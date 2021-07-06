def solution(s):
    ans=len(s)
    for i in range(1,len(s)//2+1):
        w,t,c='',0,1
        for j in range(0,len(s),i):
            # 천재적인 생각!!
            cur=s[j:j+i]
            if w != cur:
                w=cur
                t+=len(cur)
                if c>1:
                    t+=len(str(c))
                    c=1
            else:
                c+=1
        if c>1:
            t+=len(str(c))
        ans=min(ans,t)
    return ans