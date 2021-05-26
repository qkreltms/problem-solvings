#링크
'''
참고: https://cantcoding.tistory.com/13
'''
#풀이 법
'''
'''
#키포인트
'''
'''
import sys
input=sys.stdin.readline
def makeTable(P):
    lp=len(P)
    Table=[0]*lp
    i=0
    for j in range(1,lp):
        while i>0 and P[i]!=P[j]:
            i=Table[i-1]
        if P[i]==P[j]:
            i+=1
            Table[j]=i
    return Table
def KMP(P,T):
    ans=[]
    lt=len(T)
    lp=len(P)
    table=makeTable(P)
    i=0
    for j in range(lt):
        while i>0 and P[i]!=T[j]:
            i=table[i-1]
        if P[i]==T[j]:
            if i==lp-1:
                ans.append(j-lp+2)
                i=table[i]
            else:
                i+=1
    return ans


# text="abaabacaba"
# pattern="abacaba"
# text="ABC ABCDAB ABCDABCDABDE"
# pattern="ABCDABD"
text="abaabacabaabacaba"
pattern="abacaba"
ans=KMP(pattern,text)
print(len(ans))
print(*ans)
