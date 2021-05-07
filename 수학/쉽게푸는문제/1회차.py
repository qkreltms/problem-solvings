#링크
'''
문제: https://www.acmicpc.net/problem/1292
1,2,2,3,3,3,4,4,4,4,...와 같은 수열이 있을 때
A, B 구간을 자른 합을 출력하라

참고:
'''
#풀이 법
'''
'''
#키포인트
'''
range(1) = [0]
b가 1000까지므로 h를 1000까지만 생성하도록 제한하면 더 성능 최적화 가능
'''

def f(b):
    h=[]
    for i in range(1, b+1):
      for j in range(i):
        h.append(i)
    return h
a,b=list(map(int, input().split(' ')))
print(sum(f(b)[a-1:b]))