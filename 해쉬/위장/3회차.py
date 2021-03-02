'''
'''
from typing import Counter


def solution(cloths):
  ans = 1
  for _, n in Counter(map(lambda c: c[1], cloths)).items():
    ans *= n + 1
  return ans - 1


print(solution([['1', 'A'], ['1', 'B'], ['1', 'A']]))
print(solution([['1', 'A'], ['1', 'A'], ['1', 'A']]))
