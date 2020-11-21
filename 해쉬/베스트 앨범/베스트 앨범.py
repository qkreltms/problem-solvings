# HACK!!! python sort 알고리즘은 중복을 허용하지 않는다.
# 장르 총합 젤 큰 순으로...
      
from collections import Counter

def solution(genres, plays):
  visited = [False for _ in range(len(plays))]
  dic = {}
  ans = []

  for i in Counter(genres).keys():
    dic[i] = 0
  for i in range(len(plays)):
    dic[genres[i]] += plays[i]
  sortedByPlaysGenres = sorted(dic.items(), key=lambda x: x[1], reverse=True)
  for (pivot,_) in sortedByPlaysGenres:
    max = 0
    genreAns = [-1, -1]
    for i in range(len(plays)):
      if genres[i] == pivot:
        if plays[i] > max:
          max = plays[i]
          genreAns[0] = i

    visited[genreAns[0]] = True
    max = 0

    for i in range(len(plays)):
      if genres[i] == pivot:
        if visited[i] != True:
          if plays[i] > max:
            max = plays[i]
            genreAns[1] = i
    if genreAns[1] == -1:
      ans.append(genreAns[0])
    else:
      ans += genreAns
  return ans
    
# # 답: 4, 2, 3, 장르별로 2개임!!
# print(solution(['B', 'B', 'B', 'B', 'A'], [500, 150, 800, 800, 2500]))
print(solution(['A', 'B', 'A', 'A', 'B'], [500, 600, 150, 800, 2500]) == [4, 1, 3, 0])
print(solution(['B', 'A'], [500, 600]) == [1, 0])
print(solution(['B', 'A'], [600, 500]) == [0, 1])
print(solution(['A', 'B'], [600, 500]) == [0, 1])
print(solution(['A', 'A', 'B'], [600, 500, 300]) == [0, 1, 2])
print(solution(['A', 'B', 'A'], [600, 500, 600]) == [0, 2, 1])
print(solution(['A', 'B', 'A'], [600, 500, 700]) == [2, 0, 1])
print(solution(['A', 'A', 'A'], [600, 500, 700]) == [2, 0])
print(solution(['A', 'A', 'A'], [3, 2, 1]) == [0, 1])
print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]) == [4,1,3,0])
print(solution(['classic'], [2500]) == [0])
print(solution(['A', 'B', 'C'], [1, 2, 3]) == [2, 1, 0])
print(solution(['A', 'B', 'C', 'D'], [1, 2, 3, 1]) == [2, 1, 0, 3])
print(solution(['A', 'A', 'B', 'A'], [2, 2, 2, 3]) == [3, 0, 2])
print(solution(['A', 'A', 'B', 'A'], [5, 5, 6, 5]) == [0, 1, 2])


# 다른 사람이 푼 문제

# NOTE: sort는 중복값 사라지기 때문에 dic에 넣어서 정렬함
# def solution(genres, plays):
#     answer = []

#     dic1 = {}
#     dic2 = {}

#     for i, (g, p) in enumerate(zip(genres, plays)):
#         if g not in dic1:
#             dic1[g] = [(i, p)]
#         else:
#             dic1[g].append((i, p))

#         if g not in dic2:
#             dic2[g] = p
#         else:
#             dic2[g] += p

#     젤 총합 큰 장르 별로 정렬
#     for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
#         여기서 나온 장르 값으로 그 장르에서 가장 큰수 넣음, 배열 2개만 만듦 
#         for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
#             answer.append(i)

#     return answer