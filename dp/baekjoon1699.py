# 1.
n = int(input())
d = [0] * 100001
for i in range(1, n+1):
    d[i] = i
    j = 1
    while j*j <= i:
        d[i] = min(d[i], d[i-j*j]+1)
        j += 1
print(d[i])
# 2.
n = int(input())
dp = [0]*100001
for i in range(1,n+1):
	j = 1
	while j*j <= i:
		if dp[i] > dp[i-j*j]+1 or dp[i] == 0:
			dp[i] = dp[i-j*j]+1
		j += 1
print(dp[n])
# 1번 문제와 2번 문제의 입력에 10000을 넣을경우 두 알고리즘의 명확한 시간차이를 느낄 수 있다.
# 이유가 뭘까?

# d[0] = 0
# d[1] = 1
# d[2] = 2
# d[3] = 3//1, 1, 1
# d[4] = 1//2
# d[5] = 2//1, 2
# d[6] = 3// 1, 1, 2
# d[7] = 4// 1, 1, 2, 1
# d[8] = 2// 2, 2
# d[9] = 1// 3
# d[10] = 2 // 3, 1
