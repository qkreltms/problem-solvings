# 섬 개수 구하기 2667 번 + 대각선 서치까지 구현

while True:
  w, h = map(int, input().split(' '))
  if w == 0 and h == 0:
    break
  visited = [[False for _ in range(w)] for _ in range(h)]
  nodes = ['0' for _ in range(h)]
  cnt = 0

  for i in range(h):
    nodes[i] = list(input().split(' '))

  def f(y, x):
    # 범위 확인
    if (x >= 0 and y >= 0 and x < w and y < h):
      node = nodes[y][x]
      # visited 확인
      if visited[y][x] or node == '0':
        return
      visited[y][x] = True
      # 탐색 시작
      # 8 방향 위, 대각, 오른쪽, 대각, 아래, 대각, 왼쪽, 대각 search 
      f(y-1, x)
      f(y-1, x+1)
      f(y, x+1)
      f(y+1, x+1)
      f(y+1, x)
      f(y+1, x-1)
      f(y, x-1)
      f(y-1, x-1)


  cnt = 0
  for i in range(h):
    for j in range(w):
      if not visited[i][j] and not nodes[i][j] == '0':
        cnt += 1
        f(i, j)

  print(cnt)