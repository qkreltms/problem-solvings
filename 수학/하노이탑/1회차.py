#링크
'''
문제: https://www.acmicpc.net/problem/1914

참고: https://www.youtube.com/watch?v=q6RicK1FCUs&ab_channel=AbdulBari
'''
#풀이 법
'''
(pdf 참고)

n=1일 때
초기: (1)()()
()()(1)
총 1회

n=2일 때
(1,2)()()
(2)(1)()
()(1)(2)
()()(1,2)
총 3회

n=3일 때
(1,2,3)()()
(2,3)()(1)
(3)(2)(1)
(3)(1,2)()
()(1,2)(3)
(1)(2)(3)
(1)()(2,3)
()()(1,2,3)
총 7회

횟수 = 2^n-1
패턴 =
n=3일 때
a,b,c 봉이 있고 원판을 1~n이라 할 때
a에서 b로 n-1개가 이동
a에서 c로 1개의 원판 n이 이동
b에서 c로 n-1개가 이동한다.

재귀적으로 위 패턴을 그려봤을 때
n=1일 때 a,c를 출력하면 된다.
'''
#키포인트
'''
'''

def f(n,a,b,c):
  if n==1:
      print(f'{a} {c}')
      return
  f(n-1,a,c,b)
  print(f'{a} {c}')
  f(n-1,b,a,c)

n=int(input())
print(2**n-1)
if n<=20:
    f(n,1,2,3)