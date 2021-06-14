t=int(input())
for _ in range(t):
	n,m=map(int,input().split())
	if m//7>n//5:
		print(n//5)
	else:
		print((m+n)//12)