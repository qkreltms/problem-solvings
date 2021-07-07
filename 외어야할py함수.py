"te st".split(' ') # ['te', 'st']
list('test') # ['t', 'e', 's', 't']


llo="llo"
f'he {llo} world!'

# 입출력 가속화
import collections
import sys
input = sys.stdin.readline 
print = sys.stdout.write

# 정수와 배열이 같은 줄에 들어올 때, 1 5 5 5 5 5
N, *arr = map(int, input().split())

# 문자열을 한 글자씩 배열 저장
# AAA 
# AAA
# AAA
arr = [list(input()) for _ in range(N)] # [['A', ...], ['A', ...]]

# 리스트합치기
''.join([1,2,3,4]) # '1234'
'\n'.join([1,2,3,4]) # '1\n2\n3\n4'

# 최대값 받기
import sys
ans = sys.maxsize

# 10 진수 => 2,8,16 진법 변환
bin(42), oct(42), hex(42)
bin(12)+bin(12) # 2진법 더하기

# 2,8,16 진수 => 10 진수 변환
int('0b111',2)
int('0o74',8)
int('0x3c',16)

# 문자열 거꾸로
'ABCD'[::-1]

# 문자열 <=> 아스키코드
ord('a') # 문자를 아스키코드로
chr(65) # 아스키코드를 문자로

# 원소 갯수 찾기
[1,2,3,1].count(1) # 2
'aabc'.count('a') # 2

# 원소 중복 제거
list(set([1,2,1,2,1,2])) # [1,2]

# 정렬
# 0번째 순으로 오름차순 정렬하되, 0번째가 같으면 1번째 기준으로 오름차순 정렬한다.
sorted([[1,2], [1,1]], key=lambda x:(x[0], x[1])) # [[1,1],[1,2]]
# 0번째 순으로 오름차순 정렬하되, 0번째가 같으면 1번째 기준으로 내림차순 정렬한다.
sorted([[1,2], [1,1]], key=lambda x:(x[0], -x[1]))

# 삼항 연산자
'A' if 2 > 1 else 'B' # A

# 아스키코드
# 48~57 - 0-9
# 65~90 - A-Z
# 97~122 - a-z

# 인덱스로 삭제
[2,1,1].pop(0) # [1,1], return 2
# 값으로 삭제
[2,1,1].remove(2) # [1,1], return 없음

# "".find(target, startIndex) vs "".index(target) or [].index(target)
# find는 target이 없으면 -1, index는 throws an error 

# a//b vs int(a/b)
# a가 음수일 때 두개의 값이 다르게 나온다.
# 1) print(-5055//7)
# 2) print(int(-5055/7))
# 처음시도 1번에서는 -723이 나옴
# 2번에서는 -722가 나옴
# 값이 서로 다름

# 디스트럭팅할 때 주의!!
# U,V=['', 1]는 에러 발생
# U,V=('', 1)은 정상

from collections import Counter
c = Counter('(())') # Counter: { '(': 2, ')': 2}
if c[')'] == c['(']:
  print(True)
print(False)

# Counter 사용해 set이랑 동일하게 구현 가능, 다만 카운터는 중복 허용
list(Counter(['a','b','c']) - Counter(['a','b']))[0]
list(set(['a','b','c']) - set(['a','b']))[0]

# zip
print(list(zip([1,2,3], [3,4], [6,7]))) # [(1, 3, 6), (2, 4, 7)]

# 인덱스 슬라이싱때 시작, 끝 값은 어떤 값이 되든지 상관없다.
print([1,2,3,4][3:4000000]) # [4]
print('123'[40:]) # ''
print('123'[40:99999]) # ''

# deque
import collections, itertools
q=collections.deque([1,2,3,4,5])
list(itertools.islice(q,3,7))
q.extend('ab') # list와 마찬가지로 iterable 을 삽입
q.extendleft(['a','b'])
q.append('a')
q.appendleft('a')
q.pop()
q.popleft()
deq = collections.deque(['a', 'b', 'c', 'd', 'e'])
deq.rotate(1) # e a b c d
deq = collections.deque(['a', 'b', 'c', 'd', 'e'])
deq.rotate(-1) # b c d e a

# map에서 lambda 사용 법
map(lambda x: x[1], [(1,2)])
