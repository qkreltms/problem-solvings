# HACK!!! python sort 알고리즘은 중복을 허용하지 않는다.
# 장르 총합 젤 큰 순으로...

# from collections import Counter

# def solution(genres, plays):
#   visited = [False for _ in range(len(plays))]
#   visitedGenres = []

#   ans = []
#   genreCnt = len(sorted(list(Counter(genres))))


#   for c in range(genreCnt):
#     genreAns = [-1, -1]
#     max = 0
#     pivot = ''
#     for i in range(len(plays)): 
#       if visited[i] != True:
#         if plays[i] > max and genres[i] not in visitedGenres:
#           max = plays[i]
#           pivot = genres[i]
#           genreAns[0] = i

#     max = 0
#     visited[genreAns[0]] = True
#     visitedGenres.append(pivot)

#     for i in range(len(plays)): 
#       if visited[i] != True:
#         if pivot == genres[i]:
#           if plays[i] > max:
#             max = plays[i] 
#             visited[i] = True
#             genreAns[1] = i
#     if genreAns[1] == -1:
#       ans.append(genreAns[0])
#     else:
#       ans += genreAns
#   return ans
      
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