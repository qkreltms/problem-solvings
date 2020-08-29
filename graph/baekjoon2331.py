import sys
sys.setrecursionlimit(999999)

def f(A, C):
  if V[A] != 0:
    return V[A] - 1
  else:
    V[A] = C + 1
    b = A
    a = 0
    while b >= 1:
      a += (b % 10) ** P
      b //= 10
    return f(a, V[A])
    
 
A, P = map(int, input().split(" "))
V = [0] * 236197 # 더 좋은 방법? => list 사용, null을 0으로 쓰면 되지 않을까?
C = 0
print(f(A, C), end="")
