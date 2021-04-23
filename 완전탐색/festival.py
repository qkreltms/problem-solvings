c = int(input())

for k in range(0, c):
    n, l = list(map(int, input().split()))
    a = list(map(int, input().split()))

    i = 0
    avg = 1000000000
    while i <= n-l:
        sum, count = 0, 0
        j = i
        while j < l+i-1:
            count += 1
            sum += a[j]
            j += 1
        while j < n:
            count += 1
            sum += a[j]
            avg = min(avg, sum/count)
            j += 1
        i += 1
    print("%.12f" % avg)