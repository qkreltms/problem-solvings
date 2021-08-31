n = int(input())
a = list(map(int, input().split()))
gihos = list(map(int, input().split()))
maxNum = -1000000001
minNum = 1000000001


def f(cnt, hap, sub, mul, div, res):
    global maxNum, minNum
    if hap < 0 or sub < 0 or mul < 0 or div < 0:
        return
    if cnt == n-1:
        maxNum = max(res, maxNum)
        minNum = min(res, minNum)
        return
    f(cnt+1, hap-1, sub, mul, div, res+a[cnt+1])
    f(cnt+1, hap, sub-1, mul, div, res-a[cnt+1])
    f(cnt+1, hap, sub, mul-1, div, res*a[cnt+1])
    f(cnt+1, hap, sub, mul, div-1, int(res/a[cnt+1]))


f(0, gihos[0], gihos[1], gihos[2], gihos[3], a[0])
print(maxNum)
print(minNum)
