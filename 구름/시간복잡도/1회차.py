'''
https://level.goorm.io/exam/58258/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%9E%88%EC%96%B4%EB%A1%9C%EC%A6%88-%EC%85%80%ED%94%84%EB%A0%88%EB%B2%A8%ED%85%8C%EC%8A%A4%ED%8A%B8-9%EC%B0%A8/quiz/2
'''
def solution(n):
  b = n // 25
  a = n // 5
  if b:
    return a+b
  return a

print(solution(4))
print(solution(5))
print(solution(10))
print(solution(75))
print(solution(100))
print(solution(99), 22)
print(solution(110))
print(solution(1000000000), 249999998)

# 5부터 0이 나타남
# 10 2
# 15 3
# 20 4 
# 25 6 2개 증가
# 30 7
# 35 8
# 40 9
# 45 10
# 50 12 2개 증가
# 55 13
# 60 14
# 65 15
# 70 16
# 75 18 2개 증가