def solution(s):
    ans=len(s)
    for i in range(1,len(s)//2+1):
        temp=0
        cnt=1
        next=''
        for j in range(0,len(s),i):
            cur=s[j:j+i]
            if next!=cur:
                if cnt>1:
                  temp+=len(str(cnt))
                  cnt=1
                next=cur
                temp+=len(next)
            elif next==cur:
                cnt+=1
        if cnt>1:
            temp+=len(str(cnt))
        ans=min(ans,temp)
    return ans
solution('aabbaccc')