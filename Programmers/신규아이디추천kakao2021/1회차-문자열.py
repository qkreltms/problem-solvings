'''
아이디 규칙에 맞지 않는 아이디 입력시 
입력 아이디와 유사 & 규칙 맞는 아이디 추천

아이디 길이 3~15
알파벳 소문자, 숫자, -, _, . 문자 허용
단 마침표는 처음과 끝, 연속 사용 불가

1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
'''
# 풀이 법
'''
'''
import re
def solution(newId):
  recommId = newId
  recommId = newId.lower()
  p = re.compile('[a-z0-9-_.]')
  temp = ''
  for s in recommId:
    if (p.match(s)):
      temp += s
  recommId = temp

  while True:
    i = recommId.find('..')
    if i == -1:
      break  
    recommId = recommId[0:i] + recommId[i+1:]
  
  if recommId and recommId[0] == '.':
    recommId = recommId[1:]
  if recommId and recommId[-1] == '.':
    recommId = recommId[0:-1]

  if not recommId:
    recommId = 'a'
  
  if len(recommId) >= 16:
    recommId = recommId[0:15]
    if recommId[-1] == '.':
      recommId = recommId[0:-1]
  
  if len(recommId) <= 2:
    c = recommId[-1]
    while len(recommId) < 3:
      recommId += c
  return recommId 

print(solution("...!@BaT#*..y.abcdefghijklm"), "bat.y.abcdefghi")
print(solution("z-+.^."), "z--")
print(solution("=.="), "aaa")
print(solution("...."), "aaa")
print(solution("123_.def"), "123_.def")
print(solution("abcdefghijklmn.p"), "abcdefghijklmn")