# 방향이 있는 그래프로 풀어야 쉽게 풀 수 있다.
# 입력 
# 첫째 줄 테스트 케이스 개수
# 둘째 줄 그래프의 정점의 개수, 간선의 개수
import sys

# 테스트 케이스 개수 (2 <= K <= 5)
T = int(sys.stdin.readline())
# 정점, 간선
V, E = map(int, sys.stdin.readline().split(" ")
# 배열 초기화
adj = [[0] for i in range(V+1)]
# 값 입력
a, b = map(int, sys.stdin.readline().split(" ")
adj[a][b] = b