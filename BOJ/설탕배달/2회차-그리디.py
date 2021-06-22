#풀이 법
'''
1. n이 주어지면 n을 5로 나누고 
2. n%3일 때 n을 3으로 나눈다.
3. 만약 n%3이 아니라면 n에 5를 더하면서 계속 2번을 반복한다.
'''
#키포인트
'''
'''

n=int(input())
a=n//5
n=n%5
b=0
while a>=0:
  if n%3==0:
    b=n//3
    n=n%3
    break
  a-=1
  n+=5
if n == 0:
  print(a+b)
else:
  print(-1)