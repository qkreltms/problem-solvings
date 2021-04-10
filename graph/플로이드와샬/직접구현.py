'''
https://www.youtube.com/watch?v=4OQeCuLYj-4&ab_channel=MichaelSambol
https://blog.naver.com/ndb796/221234427842
https://m.blog.naver.com/PostView.nhn?blogId=zxy826&logNo=220948766884&proxyReferer=https:%2F%2Fwww.google.com%2F
모든 정점에서 모든 정점으로 가는 최소비용은?(음수 포함) # DP접근

1. 자기자신을 가리키는 곳은 0으로 초기화한다.
2. 각 노드를 순회하며 엣지 값을 넣는다.
3. 모든 노드를 순회하며 다이렉트로 가는게 빠른지 거쳐가는게 빠른지 비교한다. (알고리즘을 그냥 외워야 될듯...?)
'''
INF = float('inf')
arr = [
    [0, 5, INF, 8],
    [7, 0, 9, INF],
    [2, INF, 0, 4],
    [INF, INF, 3, 0]
]


def solution():
    d = [*arr]

    # k 거쳐가는 노드
    for k in range(len(arr)):
        for i in range(len(arr)):
            for j in range(len(arr)):
                # A => B 갈 때 A => k => B를 가는 것이 더 짧은지 비교 
                #  예 i,j = 2,3일 때 1=>3 + 2=>1 < 2=>3 비교   
                if d[i][k] + d[k][j] < d[i][j]:
                    # 위아래 비슷함
                    d[i][j] = d[i][k] + d[k][j]
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(' '+str(d[i][j]), end='')
        print('')


solution()
