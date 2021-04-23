'''
정렬된 숫자와 찾는 숫자가 주어지면 몇 번만에 찾았는지 반환한다. 

1 2 3 4 5, 2라면
3을 먼저 가리킨뒤 주어진 숫자보다 크면 왼쪽에서 찾는다.
다시 반을 찾는다. 주어진 숫자이므로 순환 값을 반환한다.
'''

def solution(N, n):
  def f(N, n, i):
    mid = len(N) // 2
    target = N[mid]
    if target == n:
      return i+1
    elif target > n:
      return f(N[0:mid], n, i+1)
    else:
      return f(N[mid:], n, i+1)
  return f(N, n, 0)

print(solution([1,2,3,4,5], 1))
print(solution([1,2,3,4,5], 2))
print(solution([1,2,3,4,5], 3))
print(solution([1,2,3,4,5], 4))
print(solution([1,2,3,4,5], 5))

