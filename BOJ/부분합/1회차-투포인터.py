#링크
'''
문제: https://www.acmicpc.net/problem/1806
'''
#풀이 법
'''
S=10일 때 아래와 같은 수열이 있다면
5 1 3 5 10 7 4 9 2 20

(5),(5,1),(5,1,3),(5,1,3,5),(1,3,5),(1,3,5,10),(3,5,10),(5,10),(10)
과 같은 방식으로 왼쪽, 오른쪽을 늘리고 줄이면서 부분합 최소 길이를 구한다.
'''
#키포인트
'''
모든 부분합을 계산할 수 있어야한다.
(5),(5,1),(5,1,3),(5,1,3,5),(5),(5,10),(10) 과 같은 방식으로는 모든 부분합을 구하지 못 한다.
'''

import sys
n,s=list(map(int,input().split()))
seqs=list(map(int,input().split()))
seqs.append(0)
def f():
    if s<=1:
        return 1
    subSum,ai,bi=0,0,0
    ans=sys.maxsize
    while bi < len(seqs):
        if subSum>=s:
            subSum-=seqs[ai]
            ai+=1
            ans=min(ans,bi-ai+1)
            if ans == 1:
                return 1
        else:
            subSum+=seqs[bi]
            bi+=1
    if ans == sys.maxsize:
        return 0
    return ans
print(f())