# https://www.acmicpc.net/problem/12920
# 문제e
'''
N개의 물건이있을 때(각 물건은 개수가 주어진다.) 각 물건은 무게 W와 가치 V를 가지는데 배당은 최대 K 무게 만큼의 
무게만 넣을 수있다. 이 때의 최대 가치는?
'''
# 풀이 법
'''
배낭채우기 1의 방법을 쓴다, but
각 아이템의 주어진 개수만큼 가치를 곱한 값을 table에 같이 넣는다.
만약 기존의 무게에 주어진 최대 값보다 더 높은 값이 들어오면 대채한다.  

메모리 초과 발생 "기존의 무게에 주어진 최대 값보다 더 높은 값이 들어오면 대채한다." 구현하기
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
w = []
v = []
for i in range(n):
  iw, iv, inum = map(int, input().split(' '))
  for j in range(inum):
    w.append(iw)
    v.append(iv)

print(knapsack(bw, w, v, len(w)))

# print(knapsack(4, [2], [2], 1), 2)
# print(knapsack(30, [5,10,20], [5,6,14], 3), 20)