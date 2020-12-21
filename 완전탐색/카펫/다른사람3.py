# https://programmers.co.kr/learn/courses/30/lessons/42842/solution_groups?language=python3
# 직각의 둘레 공식을 이용했다(?)
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]