a = ['leo', 'eden', 'eden']
b = 	['eden', 'leo']

# 주의 python 3.8 이상은 sort 알고리즘 바뀐듯
# x
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]

print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))

# Counter 쓰기
# o
from collections import Counter

def solution(a, b):
  print(list(Counter(a) - Counter(b))[0])

solution(a, b)  

# hash 쓰기
# x, 가장 느림
def solution(a, b):
  a.sort()
  b.sort()
  hashSum = 0 
  dic = {}
  for i in a:
    myHash = hash(i)
    hashSum += myHash
    dic[myHash] = i
  for j in b:
    hashSum -= hash(j)
  return dic[hashSum]
print(solution(a, b))
