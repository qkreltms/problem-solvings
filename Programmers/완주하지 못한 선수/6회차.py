from collections import Counter 
def solution(p,c):
    return list(Counter(p)-Counter(c))[0]