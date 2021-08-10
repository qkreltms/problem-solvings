def f():
	a,b=map(int,input().split())
	# B가 더 많을 때
	if b//7>=a//5:
		return a//5
	# A가 더 많을 때
	return (a+b)//12
t=int(input())
for _ in range(t):
	print(f())