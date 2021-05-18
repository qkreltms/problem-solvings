#링크
'''
문제: https://www.acmicpc.net/problem/2504
참고:
'''
#풀이 법
'''
부모 괄호가 있을 경우 그 하위 자식들은 모두 부모 괄호 값과 X 연산을 
해줘야하고 각 자식 값은 + 연산을 해줘야해야한다.

그러므로

([][])에서 "([]" 일 때
r=2X3 값을 적용하고

"([]]" 일 때
i-1번지가 ]이므로 무시한다.

"([][]" 일 때
r+=2X3
"([][])" 일 때

값 12가 나온다.
'''
#키포인트
'''
90%에서 실패함
원인은 if not stack or i-1 < 0 or s[i] != '[': 에서 s[i] != '[' 부분
반례는 찾기 힘드나, s[i] 보다는 stack에 항상 나머지 한 부분이 존재해야하므로
더 쉬운 방법인 stack을 사용하는 것이 해답이었음
'''

def f(s):
    stack=[]
    ans=0
    r=1
    if len(s) == 1:
        return 0
    for i, c in enumerate(s):
        if c == '(':
            r*=2
            stack.append('(')
        elif c == ')':
            if not stack or i-1 < 0 or stack[-1] != '(':
                return 0
            if s[i-1] == '(':
                ans+=r
            r=int(r/2)
            stack.pop()
        elif c == '[':
            r*=3
            stack.append('[')
        elif c == ']':
            if not stack or i-1 < 0 or stack[-1] != '[':
                return 0
            if s[i-1] == '[':
                ans+=r
            r=int(r/3)
            stack.pop()
    if stack:
       return 0
    return ans
# s=list(input())
# print(f(s))


# print(f('()[]'),5)
# print(f('()'),2)
# print(f(')'),0)
# print(f(']'),0)
# print(f(')(()'),0)
# print(f('(]'),0)
print(f('[[[[]]]]'),81)
# print(f('(([]))(()())'),20)
# print(f('(([]))(()()))'),0)
