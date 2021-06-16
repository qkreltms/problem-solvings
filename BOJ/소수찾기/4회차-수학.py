n=int(input())
targets=list(map(int,input().split()))
h=[True for _ in range(1001)]
h[1]=False
for i in range(2,int(max(targets)**0.5)+1):
    for j in range(i*2,1001,i):
        h[j]=False
cnt=0
for i in range(n):
    if h[targets[i]]:
        cnt+=1
print(cnt)