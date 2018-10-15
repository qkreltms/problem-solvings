def f(i):
    if i <= 1:
        return 1
    if arr[i] > 0:
        return arr[i]
    if i-1 >= 0:
        arr[i] += f(i-1)
    if i-2 >= 0:
        arr[i] += f(i-2)
    if i-3 >= 0:
        arr[i] += f(i-3)
    return arr[i]


for i in range(int(input())): # 들어올 개수
    n = int(input())
    arr = [0] * (n + 1)
    print(f(n))


