# 문제
'''
링크: https://programmers.co.kr/learn/courses/30/lessons/42895

아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고
이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만
사용해서 표현 할 수 있는 방법 중 N 사용횟수의
최솟값을 return 하도록 solution 함수를 작성하세요.

N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.
'''
# 문제풀이
'''
재귀적으로 순회하며 모든 경우의 수를 구한다.
[]+1
[]/1
[]-1
[]*1
단, 11+1,.. 과 같은 경우도 있으니 재귀적으로 순회하는 동안 n번만큼 순회하며
1, 11, ... 과 같은 숫자까지 계산할 수 있게한다.
왜  8번만큼만 순회하냐면 n 개수가 8개까지만 되므로 그 이후는 볼 필요없음(초과 되니까)

5+(5/5)
5/(55+5) =>
(55+5)/5와 같은 괄호 문제는 어떻게 해결하지...?
=> 곱하기와 나누기에서 괄호 문제가 발생한다.
------------------------

괄호 문제는 아래로 해결한다.
n = 5라고 할 때
n이 한 개일때
1) 5
2개일 때
2) 55, 5+5, 5-5, 5x5, 5/5

3) 555
1) + 2) 5+55, 5-55, ...
2) + 1) 55+5, 55-5, ...

4) 5555
1) + 3) 5+555, 5-555, ...
2) + 2) 55+55, 55-55, ...
3) + 1) 555+5, 555-5, ...

이렇게 차근차근히 한 자리씩 높여가며 number를 찾는다.

구현:
set을 8개 만들고
5~55555555를 초기값으로 준다

루프를 돌면서 위와 같은 순서로, 아래와 같이 넣는다.
[(5), (55, 5+5, 5-5,...), ...]
단, 첫 번째[0], 마지막 인덱스 [7]에는 아무 값도 넣지 말아야한다.
'''


def solution(N, number):
    if N == number:
        return 1

    mySets = [set() for _ in range(8)]
    for i, s in enumerate(mySets, start=1):
        s.add(int(str(N)*i))

    ans = -1
    for i in range(1, 8):
        for j in range(i):
            # 0번 째부터 7번째까지 돈다, N은 1~9
            for a in mySets[j]:
                for b in mySets[i-1-j]:
                    mySets[i].add(a+b)
                    mySets[i].add(a-b)
                    mySets[i].add(a*b)
                    if b != 0:
                        mySets[i].add(a//b)
        if number in mySets[i]:
            ans = i+1
            break

    return ans


print(solution(5, 12), 4)
print(solution(2, 11), 3)
print(solution(1, 1121), 7)
print(solution(8, 53), 5)
print(solution(8, 888888888), 9)


# -----------예전 코드-----------
'''
# import sys
# sys.setrecursionlimit(99999999)


# def f(result, cnt):
#     global ans
#     if result == target:
#         if ans > cnt or ans == -1:
#             ans = cnt
#             print(cnt)
#         return
#     if cnt > 8:
#         return
#     for i in range(0, 8-cnt):
#         n = template[i]
#         cnt += 1
#         f(result+n, cnt)
#         f(result-n, cnt)
#         f(result//n, cnt)
#         f(result*n, cnt)
#         f(result+(n*n), cnt)
#         f(result+(n//n), cnt)


# def solution(N, number):
#     global ans
#     global target
#     global template
#     global n
#     n = N
#     template = list(map(int, [str(N)*1, str(N)*2, str(N)*3, str(N)*4,
#                               str(N)*5, str(N)*6, str(N)*7, str(N)*8]))
#     target = number
#     ans = -1
#     f(0, 0)
#     return ans
'''
