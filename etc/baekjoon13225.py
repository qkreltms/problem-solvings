#https://www.acmicpc.net/problem/13225
n = int(input())
ans = [0]
for i in range(n):
    ans.append(int(input()))

for i in range(1, len(ans)):
    cnt = 0
    for j in range(1, ans[i]+1):  # j*j를 하는 이유는 sqrt(n)가 안되는 숫자도 있으므로
        if j*j <= ans[i]:
            if ans[i] % j is 0:
                cnt += 1
                if j*j < ans[i]:
                    cnt += 1
        else:
            break
    print(ans[i], cnt)
