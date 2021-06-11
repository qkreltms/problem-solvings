'''
문자열이 주어지면 모음(aeiou)만 반환하시오,
단 모음이 없으면 ???
'''

import re
def f(param):
  p = re.compile('[^aeiou]', re.IGNORECASE)
  return p.sub('', param) or '???'

# n = int(input())
# for _ in range(n):
#   param = input()
#   print(f(param))


print(f('Hello, World!'))
print(f("I'm your father."))
print(f("What are you doing here?"))
