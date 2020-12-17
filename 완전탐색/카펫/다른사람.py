'''
https://programmers.co.kr/questions/12197
'''
import math

def solution(brown, yellow):
    term = math.sqrt((brown+4)**2 /4 - 4 * (brown + yellow))
    w = ((brown + 4) / 2 + term) / 2
    h = ((brown + 4) / 2 - term) / 2
    return [w,h]