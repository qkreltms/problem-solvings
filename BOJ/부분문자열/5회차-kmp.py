def makeTable(p):
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
    s=input()
    p=input()
    table=makeTable(p)
    j=0
    for i in range(len(s)):
        while j>0 and p[j]!=s[i]:
            j=table[j-1]
        if p[j]==s[i]:
            j+=1
            if len(p)==j:
                return 1
    return 0
print(kmp())