# https://www.acmicpc.net/problem/12865
# 문제e
'''
N개의 물건이있을 때(각 물건은 한 개만있음) 각 물건은 무게 W와 가치 V를 가지는데 배당은 최대 K 무게 만큼의 
무게만 넣을 수있다. 이 때의 최대 가치는?
'''
# 풀이 법
'''
* 입력 정렬 필요없음

분할정복이 가능한 문제로 DP 적용이 가능하다.

2차원 배열을 쓰고 B[n][w]로 한다.
B[ni][wi]에 값을 넣을 때 이전 아이템의 최대 가치 값과 B[n(i-1)][wi] 또는
(현재 아이템의 가치)vi + 현재 아이템의 무게를 뺀 이전 아이템의 최대가치 B[n(i-1)][K-wi]
의 최대값을 넣는다.(왜냐면 이렇게 해야 이전 무게와 섞일 수 있고 최대 가치가 보장됨, 기본적으로 최소 2가닥은 있는게 좋다.)
''' 

def knapsack(bw, w, v, n):
  table = [[0 for _ in range(bw+1)] for _ in range(n+1)]

  for i in range(1, n+1):
    for j in range(1, bw+1):
      if w[i-1] <= j:
        table[i][j] = max(table[i-1][j], v[i-1]+table[i-1][j-w[i-1]])
      else:
        table[i][j] = table[i-1][j]
  return table[n][bw]

n, bw = map(int, input().split(' '))
w = [0 for _ in range(n)]
v = [0 for _ in range(bw)]
for i in range(n):
  iw, iv = map(int, input().split(' '))
  w[i] = iw
  v[i] = iv
print(knapsack(bw, w, v, n))

# print(knapsack(4, [2], [2], 1), 2)
# print(knapsack(30, [5,10,20], [5,6,14], 3), 20)