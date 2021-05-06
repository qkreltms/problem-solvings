#링크
'''
문제: https://www.acmicpc.net/problem/3460
양의정수 n이 주어질 때 이진수 변환, 1의 위치를 모두 찾아 반환
단, 최하위 비트는 0번째(젤 오른쪽이 0) t, n은 1부터, 출력값 공백으로 나눔
참고:
'''
#풀이 법
'''
bin으로 바꾼 후 string 나옴 [2:] ('0b') 자른 후 reverse() 해주고 // 젤 오른쪽이 0이므로
enumerate 돌면서 bit가 1인지 판단, 맞다면 index저장 후 결과 출력
'''
#키포인트
'''
bin(13) // '0b1101'
'''

def f():
    n = int(input())
    bits = reversed(bin(n)[2:])
    ans = []
    for i, b in enumerate(bits):
        if b == '1':
            ans.append(str(i))
    return ' '.join(ans)
t = int(input())
for _ in range(t):
    print(f())