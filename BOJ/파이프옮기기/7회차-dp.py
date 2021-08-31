n=int(input())
h=[[] for _ in range(n)]
for i in range(n):
    h[i]=input().split()
d=[[[0,0,0] for _ in range(n)] for _ in range(n)]
d[0][1][0]=1
# 위쪽에 일짜벽을 쭉 깔아준다. 왜냐하면 어차피 - 자 벽이 깔리므로
for i,_ in enumerate(d[0][2:]):
    # 위쪽에 벽이 하나라도 있으면 그 다음은 못 가니까 스탑
    if h[0][2+i]=='1':
        break
    d[0][2+i][0]=1
for i in range(1,n):
    for j in range(1,n):
        # 벽을 마주치면 다음 프로세스를 진행한다.
        if h[i][j]=='1':
            continue
        # 가로, 세로, 대각선
        d[i][j][0]=d[i][j-1][0]+d[i][j-1][2]
        d[i][j][1]=d[i-1][j][1]+d[i-1][j][2]
        # 대각선은 세영역을 확인하라는 조건에 따라서 위, 왼쪽에 벽이 있는지 확인해야 한다.
        if h[i-1][j]!='1' and h[i][j-1]!='1':
            d[i][j][2]=sum(d[i-1][j-1])
print(sum(d[n-1][n-1]))
        