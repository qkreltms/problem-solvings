n,k=map(int,input().split())
c=0
# 약수를 구할 때 n*0.5+1 정도만 루프 돌아주는게 성능상 이득이다.
for i in range(1, n//2+1):
    if n%i==0:
        c+=1
        if c==k:break
if c==k:
    print(i)
elif c+1==k:
    print(n)
else:
    print(0)