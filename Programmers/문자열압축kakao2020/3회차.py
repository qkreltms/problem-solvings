import sys
def solution(s):
    def f():
        if len(s) < 4:
            return len(s)
        ans=len(s)
        for i in range(1,len(s)//2+1):
            curPick=''
            c=1
            l=0
            for j in range(0,len(s),i):
                nextPick = s[j:j+i]
                if curPick != nextPick:
                    if c > 1:
                        l+=len(str(c))
                        c=1
                    curPick=nextPick
                    l+=len(curPick)
                else:
                    c+=1
            if c > 1:
                l+=len(str(c))
            ans=min(ans,l)
        return ans
    return f()
print(solution("aabbaccc"), 7)
                
                
            
        