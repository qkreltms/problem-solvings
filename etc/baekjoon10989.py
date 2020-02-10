import sys

n = int(input())
limit = 10001
A = [0] * limit

# 입력
for _ in range(n):
    A[int(sys.stdin.readline())] += 1  # 해당 번지에 1++

# 출력
for i in range(0, limit):
    if A[i]:  # 값이 1 이상일 경우
        for j in range(A[i]):  # 해당 번지에 중복된 수 만큼 출력
            sys.stdout.write(str(i) + "\n")

# import sys
# f = open(0)
# f.readline()
# A = [0] * 10001
# for i in f:
#     A[int(i)] += 1
# for i in range(10001):
#     sys.stdout.write((str(i) + '\n') * A[i])
