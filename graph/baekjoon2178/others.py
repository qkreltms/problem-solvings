n,m=map(int,input().split())
e=set()
for x in range(n):
    for y,c in enumerate(input()):
        if c=="1":
            e.add((x,y))
q=[((0,0),1)]
h=set()
while q[0][0]!=(n-1,m-1):
  x,y=q[0][0]
  for i in {-1,1}:
    for j in {(x+i,y),(x,y+i)}:
      if j in e and j not in h:
        h.add(j)
        q.append((j,q[0][1]+1))
  del q[0]
print(q[0][1])