def f():
	a,b=map(int,input().split())
	if b//7>=a//5:
		return a//5
	return (a+b)//12
t=int(input())
for _ in range(t):
	print(f())