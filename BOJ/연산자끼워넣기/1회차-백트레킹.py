#링크
'''
문제: https://www.acmicpc.net/problem/14888
수와 수 사이에 연산자를 넣어 수식을 만들되 수의 순서를 바꾸지 말라
연산자 우선순위 무시 앞에서부터 진행
나눗셈은 정수 몫만 취한다
만들수 있는 식의 결과의 최대, 최소값 출력

참고:
'''
#풀이 법
'''
DFS로 접근해 모든 경우의 수를 구한다.
'''
#키포인트
'''
나눗셈은 정수 몫만 취한다에서
1) print(-5055//7)
2) print(int(-5055/7))
처음시도 1번에서는 -723이 나옴
2번에서는 -722가 나옴
값이 서로 다름
'''
maxNum = -1000000001
minNum = 1000000001

n=int(input())
nums=list(map(int,input().split(' ')))
gihos=list(map(int,input().split(' ')))

def f(i,plus,minus,mul,div,s):
    global maxNum
    global minNum
    if plus < 0 or minus < 0 or mul < 0 or div < 0:
        return
     
    if i == n:
        maxNum = max(maxNum, s)
        minNum = min(minNum, s)
        return

    f(i+1,plus-1,minus,mul,div,s+nums[i])
    f(i+1,plus,minus-1,mul,div,s-nums[i])
    f(i+1,plus,minus,mul-1,div,s*nums[i])
    f(i+1,plus,minus,mul,div-1,int(s/nums[i]))

f(1,gihos[0],gihos[1],gihos[2],gihos[3],nums[0])
print(maxNum)
print(minNum)