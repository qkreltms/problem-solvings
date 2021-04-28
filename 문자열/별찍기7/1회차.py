n = int(input())
n = 2*n-1
c = n//2+1
t = []
for i in range(c):
    s = f"{' '*(c-i-1)}{'*'*(i*2+1)}"
    print(s)
    t.append(s)
t.pop()
t.reverse()
for s in t:
    print(s)