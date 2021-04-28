"te st".split(' ') # ['te', 'st']
list('test') # ['t', 'e', 's', 't']


llo="llo"
f'he {llo} world!'

# 입출력 가속화
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

# [1,2,3,4]
''.join(A) # '1234'
'\n'.join(A) # '1\n2\n3\n4'

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