# 포인트:
# 색다르게 set으로 함
# collection안 쓰고 배열로 큐처럼 씀
# 0인 값들은 애초에 방문할 셋에 넣지를 않음
# 알고리즘 메모리: 30408, 속도: 96ms

n,m=map(int,input().split())
e=set()
for x in range(n):
    for y,c in enumerate(input()):
        if c=="1":
            e.add((x,y))
q=[((0,0),1)]
# visited
h=set()
# 마지막 일 때까지 while문 돈다
while q[0][0]!=(n-1,m-1):
  # 계속 0번째 배열 값을 받음으로써 큐처럼 쓸 수 있다.
  x,y=q[0][0]
  # 4 방향 순회
  for i in {-1,1}:
    for j in {(x+i,y),(x,y+i)}:
      # 4 방향 순회하다가 방문하지 않은 1을 만나면 큐에 추가한다.
      if j in e and j not in h:
        h.add(j)
        # 거리를 한 칸 추가해 준후 큐에 넣는다.
        q.append((j,q[0][1]+1))
  # 제거해 준다.
  del q[0]
# 마지막 것은 넣기만하고 pop은 안하므로 그 것의 거리 값을 출력한다.
print(q[0][1])