A=[]
def f():
    l = len(A)
    s = sum(A)
    for i in range(l):
        for j in range(i+1, l):
            if (s - (A[i]+A[j])) == 100:
                A.pop(i)
                A.pop(j-1)
                return A
    
for _ in range(9):
    A.append(int(input()))
A.sort()
for a in f():
    print(a)