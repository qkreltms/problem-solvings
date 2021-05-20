def solution(s):
    def cut():
        results=[[] for _ in range(len(s)//2)]
        i,j=1,0
        while (len(s)//2)>=i:
            temp=[]
            curI,nextI=0,i
            while nextI < len(s):
                temp.append(s[curI:nextI])
                curI=nextI
                nextI+=i
            temp.append(s[curI:])
            results[j]=temp
            j+=1
            i+=1
        return results
    def f():
        if len(s) < 4:
               return len(s)
        ans=len(s)
        tokens=cut()
        for token in tokens:
            temp=''
            while token:
                cnt=1
                pick=token.pop(0)
                while token:
                    if pick == token[0]:
                        cnt+=1
                        token.pop(0)
                    else:
                        break          
                if cnt > 1:
                    temp+=(f'{cnt}{pick}')
                else:
                    temp+=pick
            ans=min(ans,len(temp))
        return ans
    return f()
                