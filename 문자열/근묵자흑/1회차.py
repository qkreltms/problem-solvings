'''
'''
import math
def f():
	N, K = list(map(int, input().split(' ')))

	a = abs(N - K)
	b = math.ceil(a / (K-1))
	print(b+1)
f()