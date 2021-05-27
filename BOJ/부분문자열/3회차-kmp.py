s=input()
p=input()
def makeTable():
    table=[0 for _ in range(len(p))]
    j=0
    for i in range(1,len(p)):
        while j>0 and p[j]!=p[i]:
            j=table[j-1]
        if p[j]==p[i]:
            j+=1
            table[i]=j
    return table
def kmp():
    table=makeTable()
    j=0
    for i in range(len(s)):
        while j>0 and s[i]!=p[j]:
            j=table[j-1]
        if s[i]==p[j]:
            j+=1
            if j==len(p):
                return 1
    return 0
print(kmp())