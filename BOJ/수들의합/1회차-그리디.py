#링크
'''
문제: https://www.acmicpc.net/problem/1789
참고: https://nanyoungkim.tistory.com/114
'''
#풀이 법
'''
1부터 n까지 더하면서 s가 넘어서면 그 n번째를 반환한다.
예:
s=14 라면
n을 5까지 hap을 구한 후
1,2,3,4,5=15
여기서 1을 빼면 14가 된다 즉 4개, (1부터 n까지의 합을 구한 후 그 중 아무거나 하나 빼면 s가 된다.) 
'''
#키포인트
'''
자연수란 1부터 시작하는 음이아닌 정수
지문의 n의 최댓값을 구하라는 말에서 헷갈릴수 있지만 앞에 "서로 다른 n개의 합"에서 갯수를 말한다는 것을 알수있음
'''

s=int(input())
i=1
hap=0
while True:
    hap+=i
    if hap>s:
        i-=1
        break
    i+=1
print(i)