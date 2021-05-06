#풀이 법
'''
bit로 바꾸면서 나머지가 1인지 판별 후 맞다면 index 결과값 저장 그 후 결과 출력
'''
def f(n):
    ans = []
    i = 0
    while n:
        if n%2==1:
            ans.append(str(i))
        i+=1
        n = n//2
    return ' '.join(ans)
t = int(input())
for _ in range(t):
    print(f(int(input())))
