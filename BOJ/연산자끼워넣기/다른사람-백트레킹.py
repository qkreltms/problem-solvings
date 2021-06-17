def dfs(index, result, add, sub, mul, div):
    global n, maxn, minn
    if index == n:
        maxn = max(result, maxn)
        minn = min(result, minn)
        return
    else:
        if add:
            dfs(index +1, result + s[index], add-1,sub,mul,div)
        if sub:
            dfs(index +1, result - s[index], add,sub-1,mul,div)
        if mul:
            dfs(index +1, result * s[index], add,sub,mul-1,div)
        if div:
            dfs(index +1, int(result / s[index]), add,sub,mul,div-1)
n = int(input())
s = list(map(int, input().split()))
a, b, c, d = map(int, input().split())

maxn = -1e9
minn = 1e9
dfs(1, s[0],a, b, c, d)
print(maxn)
print(minn)