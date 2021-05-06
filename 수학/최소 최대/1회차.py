#링크
'''
문제: https://www.acmicpc.net/problem/10818
최솟값과 최댓값을 구하라
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 
모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

참고:
'''
#풀이 법
'''
'''
#키포인트
'''
N은 1개부터 이다. 즉, n = 10 일 때 min=10, max=10
'''

import sys

def f(A):
    minN = sys.maxsize
    maxN = -9999999
    for a in A:
        a = int(a, 10)
        if minN > a:
            minN = a
        if maxN < a:
            maxN = a
    return f'{minN} {maxN}'
_ = input()
A = input().split(' ')
print(f(A))
     
    