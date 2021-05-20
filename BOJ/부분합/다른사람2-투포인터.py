import sys
input = sys.stdin.readline

def main():
  n, s = map(int, input().split())
  a = list(map(int, input().split()))
  hi, lo = 0, 0
  temp = 0
  length = []

  while True:
    if temp >= s:
      length.append(hi-lo)
      temp -= a[lo]
      lo += 1
    # 길이 탐지 조건문을 여기에 배치함으로써 왼쪽 포인터가 잘 작동되도록함
    elif hi == n:
      break
    elif temp < s:
      temp += a[hi]
      hi += 1

  if length:
    print(min(length))
  else:
    print(0)
  
main()