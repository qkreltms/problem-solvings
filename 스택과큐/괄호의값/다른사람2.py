#링크
'''
문제: 
참고: https://it-garden.tistory.com/279
'''
#풀이 법
'''
((()))와 같이 있을 때
(는 계속 stack에 담고 반대 편 )가 나왔을 때
()를 2로 바꿔주고 stack에 담는다.
두 번째 )  에서 또 위와 반복하는데 단, 숫자는 pop한 후 t에 기록한다.
다음 번에 t가 값이 있으면 2*t를 한후 stack에 넣는다.
반복하면 2*2*2 = 8이 된다.
'''
#키포인트
'''
'''

s = list(input())
stack = []
c = 0
for i in s:
    if i == ')':
        t = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '(':
                if t == 0:
                    stack.append(2)
                else:
                    stack.append(2*t)
                break
            elif top == '[':
                print(0)
                exit(0)
            else:
                t = t+int(top)
    elif i == ']':
        t = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '[':
                if t == 0:
                    stack.append(3)
                else:
                    stack.append(3*t)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                t = t+int(top)
    else:
        stack.append(i)
for i in stack:
    if i == '(' or i == '[':
        print(0)
        exit(0)
    else:
        c += i
print(c)
