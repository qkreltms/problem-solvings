# 문제
'''
설탕을 3, 5킬로 담을 수 있는 봉지가 있을 때 n이 주어진다면 
이것을 담을 수 있는 최소 봉지 갯수는?
'''
# 풀이법
'''
a = 5의 개수
b = 3의 개수
n이 주어지면 5로 나눈 값을 구한 후 + 1(a)한다.
그 후 루프를 돌면서 a*5+b*3이 n과 같은지 찾는다.
같지 않다면 5를 하나 줄여주고 3을 채워주는 식으로 찾는다.
최종적으로 못 찾으면 -1반환
'''


def f(n):
    # n = int(input())
    a = n//5+1
    if n%5 == 0:
        return a/5
    b = 0
    while a >= 0:
        if a*5+b*3 == n:
            # print(a+b)
            # return
            return a+b
        a -= 1
        b += 1
    # print(-1)
    return -1


print(f(5), 1)
print(f(3), 1)
print(f(6), 2)
print(f(18), 4)
print(f(11), 3)
print(f(4), -1)
