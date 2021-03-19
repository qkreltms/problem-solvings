'''
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
두 값을 더한 다음 //12 를 해준다

왜냐면 50, 7일 때 45//12= 3, (5+7)//12=1
즉, 57//12 = 4

(6+6)/12 =1
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