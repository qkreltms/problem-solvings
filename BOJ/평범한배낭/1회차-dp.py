#링크
'''
문제: https://www.acmicpc.net/problem/12865
'''
#풀이 법
'''
주어진 물건 1개만 사용해서 한계에 부합하는 최대 가치 만들자.
'''
#키포인트
'''
이차원 배열 사용
max(이전 무게, 현재 무게 + j번째 - 현재의 무게 번지를 위에 값과 더함[부족한 무게를 이전에서 가져옴]) 비교한다.

이차원 배열이고 마지막 무게는 앞쪽에 비어있으므로 
예를 들어 마지막 무게의 무게가 6일 때 0,1,2,3,4,5는 비어있게 되므로 이 때의 인덱스 가리킬 시 
오답이 나온다. 그러므로 모든 배열을 돌면서 j가 현재 무게 이전일 때는 이전 값을 주도록 구현 

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