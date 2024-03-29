# 문제
'''
링크: https://level.goorm.io/exam/47878/%EC%82%AC%EC%9D%80%ED%92%88-%EA%B5%90%ED%99%98%ED%95%98%EA%B8%B0/quiz/1

쿠폰 => 상품 교환
N 최소 5장
M 최소 7장 
총 12장 필요
단, N으로 부족한 개수 충족가능
최대 값은?
'''
# 풀이 법
'''
M//7가 클 때는
그냥 N//5값을 반환하는게 최적의 값이고
아닐 때는
M//7, N//5 두 값을 더한 다음 //12 를 해준다

N//5이 더 작을 때는 M//7이 아무리 커도 필요없음 => N//5
N=5, M=123123
N 5개 M 7개 끝, N에 완전 의존적인 결과값. 즉, N//5가 값이 됨

N//5이 더 크다면 N//5이 더 남는다는 것이므로 M 더해서 12를 나눠도 되고, N값만 12로 나눠도 됨 그러므로 (N+M)//12
(6+0)//12=0
(6+6)//12=1
'''
# 배운 점
'''
문제에 주어진 예제 모두 생각해보고 풀자
+ 지문에 주어진 예제도 포함
'''
def f(N, M):
    # N, M = list(map(int, input().split(' ')))
    a = N//5
    b = M//7
    if b >= a:
      return a
    return (N+M)//12

    

# T = int(input())
# while T:
#     print(f())
#     T -= 1
print(f(12, 12), 2)
print(f(12, 13), 2)
print(f(6, 6), 1)
print(f(50, 7), 4)
print(f(500, 7), 42)
print(f(6, 6), 1)
print(f(12, 12), 2)
print(f(12, 13), 2)
print(f(15, 14), 2)
print(f(999, 0), 83)
print(f(5, 99999), 1)
print(f(6, 7), 1)
print(f(4, 20), 0)