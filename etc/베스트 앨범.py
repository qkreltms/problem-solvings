# HACK!!! python sort 알고리즘은 중복을 허용하지 않는다.
from collections import Counter

def solution(genres, plays):
  visited = [False for _ in range(len(plays))]
  
  ans = []
  genreCnt = len(sorted(list(Counter(genres))))

  for c in range(genreCnt):
    genreAns = [-1, -1]
    max = 0
    pivot = ''
    for i in range(len(plays)): 
      if visited[i] != True:
        if plays[i] > max:
          max = plays[i]
          pivot = genres[i]
          genreAns[0] = i

    max = 0
    visited[genreAns[0]] = True

    for i in range(len(plays)): 
      if visited[i] != True:
        if pivot == genres[i]:
          if plays[i] > max:
            max = plays[i] 
            visited[i] = True
            genreAns[1] = i
    if genreAns[1] == -1:
      ans.append(genreAns[0])
    else:
      ans += genreAns
  return ans
      


# # 답: 4, 2, 3, 장르별로 2개임!!
# print(solution(['B', 'B', 'B', 'B', 'A'], [500, 150, 800, 800, 2500]))
# print(solution(['A', 'B', 'A', 'A', 'B'], [500, 600, 150, 800, 2500]))
print(solution(['B', 'A'], [500, 600]))