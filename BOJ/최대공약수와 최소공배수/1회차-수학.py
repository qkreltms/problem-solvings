#링크
'''
문제: https://www.acmicpc.net/problem/2609
참고: https://dimenchoi.tistory.com/46?category=750556
'''
#풀이 법
'''
유클리드 호제법, AB = LG 식 적용 
'''
#키포인트
'''
결과 값을 정확히 보자 소수점이 없어야 됨!

제한시간내에는 최대한 디버거를 사용하지 말자!!
'''


def gcd(a,b):
    while b:
        r=a%b
        a=b
        b=r
    return a
def lcm(a,b,g):
    return a*b//g
a,b=list(map(int, input().split(' ')))
g=gcd(a,b)
print(g)
print(lcm(a,b,g))