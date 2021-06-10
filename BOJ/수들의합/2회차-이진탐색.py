#키포인트
'''
1부터 n까지의 합 공식: n*(n+1)/2
'''
s=int(input())
start=1
end=s
ans=0
# start<=end까지 해야 더 정밀하게 계산 가능
while start<=end:
    mid=(start+end)//2
    hap=mid*(mid+1)//2
    # 중간값으로 구한 합과 입력으로 들어온 합을 비교한다.
    if hap>s:
        end=mid-1
    else:
        start=mid+1
        ans=mid
print(ans)
