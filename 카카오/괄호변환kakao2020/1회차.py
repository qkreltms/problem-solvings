#문제
'''
(, )의 개수가 맞다면 => 균형잡힌 괄호 문자열
(, )의 짝이 모두 맞다면 올바른 괄호 문자열 예: (()) () 균형잡힌 but 올바른 x
반면에 (()) () 균형잡힌, 올바른 o

균형잡힌 괄호 일 때 올바른 괄호 문자열로 변환할 수 있다.


1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.

예: ()))((()
#1
u = () // 앞에서부터 균형잡힌 괄호
v = f( "))((()" ) // "(())()" #2 함수 반환값
반환 ()(())()
#2
3번에 해당됨
u = ))((
v = f( "()" ) // "()" #3 함수 반환값
반환 (())()
#3
4번에 해당됨
u = ()
v = f( "" )
반환 ()
'''

def isCorrect(string):
  i = 0
  l = len(string)//2
  while string:
    if i > l:
      return False 
    j = string.find("()")
    if j == -1:
      return False
    if j+2 > len(string):
      string = string[0:j]
    else:
      string = string[0:j] + string[j+2:]
    i+=1
  return True

def isPair(string):
  cnt = 0
  for s in string:
    if s == "(":
      cnt += 1
    elif s == ")":
      cnt -= 1
  if cnt == 0:
    return True
  return False

def getUV(string):
  target = ''
  s = string
  while s:
    target += s[0:2]
    s = s[2:]
    if isPair(target):
      break
  return [target, s]

def f(string):
  if not string:
    return ''
  u, v = getUV(string)
  if isCorrect(u):
    v = f(v)
    return f'{u}{v}'
  u = u[1:]
  u = u[:-1]
  u = list(u)
  for i in range(len(u)):
    if u[i] == '(':
      u[i] = ')'
    else:
      u[i] = '(' 
  u = ''.join(u)
  return f'({f(v)}){u}'

def solution(string):
  return f(string)

print(f("()))((()"), '()(())()')

  

