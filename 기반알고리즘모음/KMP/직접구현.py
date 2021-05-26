
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
  ans=[]
  table=makeTable(p)
  for i in range(len(s)):
    while j>0 and p[j]!=s[i]:
      j=table[j-1]
    if s[i]==p[j]:
      j+=1
      if j==len(p):
        ans.append((i+1-len(p),i+1))
        j=table[j-1]
  return ans
# s="abaabacaba"
# p="abacaba"
# print(kmp(s,p), [(3,9)])
s="abaabacabaabacaba"
p="abacaba"
print(kmp(s,p), [(3,10),(10,17)])
