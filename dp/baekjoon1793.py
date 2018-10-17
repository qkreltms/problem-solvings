def f(n):
    d = [0] * (n+2) # 0들어올 때 오버플로이므로 그냥 한 개 증가시켜줌
    d[0] = 1
    d[1] = 1
    for i in range(2, n+1):
        d[i] = d[i-1] + 2 * d[i-2]
    return d[n]
while True:
    try:
        print(f(int(input())))
    except EOFError:
        break
