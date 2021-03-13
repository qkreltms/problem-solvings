'''
https://www.youtube.com/watch?v=4OQeCuLYj-4&ab_channel=MichaelSambol
https://blog.naver.com/ndb796/221234427842
모든 정점에서 모든 정점으로 가는 최소비용은?
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
