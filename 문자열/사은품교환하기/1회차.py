'''
'''
def f():
    N, M = list(map(int, input().split(' ')))
    a = N//5
    b = M//7
    if b <= 0:
      return N//12
    if a <= 0:
      return 0
    # a가 크면 a 값을 그대로 주던지
    # b와 적절하게 타협해서 줘야한다.
    if a > b:
      return (N-b*5)//12+b
    return a

T = int(input())
while T:
    print(f())
    T -= 1
