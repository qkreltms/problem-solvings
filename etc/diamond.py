def f(h):
    step = []
    for i in range(0, h//2+1):
        spaces = ' '*(h//2-i)
        stars = '*'*(1+(i*2))
        print(spaces+stars)
        step.append(spaces+stars)
    step.pop()
    for i in reversed(step):
        print(i)


f(1)
f(3)
f(5)
f(7)
f(9)
