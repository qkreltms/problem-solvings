def makeTable(p):
  j=0
  table=[0 for _ in range(len(p))]
  for i in range(1,len(p)):
    while j>0 and p[j]!=p[i]:
      j=table[j-1]
    if p[i]==p[j]:
      j+=1
      table[i]=j
  return table
def kmp(s,p):
  j=0
  table=makeTable(p)
  for i in range(len(s)):
    while j>0 and p[j]!=s[i]:
      j=table[j-1]
    if s[i]==p[j]:
      j+=1
      if j==len(p):
        return 1
  return 0
s=input()
p=input()
print(kmp(s,p))