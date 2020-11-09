import math
from collections import Counter

test = [['yellow_hat', 'face'], ['blue_sunglasses', 'face'], ['green_turban', 'face'], ['green_turban', 'face2']]

def solution(clothes):
  classifiedClothes = []
  for [_, sort] in clothes:
    classifiedClothes.append(sort)
  # 종류별로 개수를 정한다.
  dic = Counter(classifiedClothes)

  ans = 1
  #같은 종류의 옷은 조합에 포함되지 않기 때문에 다른 종류의 아이템을 곱한다, 단 없을 경우 아이템 + 1
  #예: 상의: A,B,C 하의: A 가 있을 때 3*1=3 개의 조합이 나오는데 이 경우
  #모두다 존재할 때의 경우의 수 이므로 각 아이템에서 없을 때의 경우를 하나 넣어줘서
  # 곱을한다. X=이 아이템이 없을 때의 경우, 상의: A,B,C,X, 하의: A,X 4*2 = 8
  # 두 아이템 다 없을 때의 경우의 아이템이 있으므로 모두다 없을 때가 있을 것이다.
  # 그러므로 모두다 없는 경우의 수 (1)를 마지막에 빼준다.
  for i in list(dic.values()):
    #(아이템 개수) * (아무것도 없을 경우의 아이템 개수) 
    ans *= i + 1
  
  #(모든 아이템이 없을 경우의 수를 뺀다.)
  return ans - 1

print(solution(test))