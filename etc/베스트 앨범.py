# HACK!!! python sort 알고리즘은 중복을 허용하지 않는다.
# def solution(genres, plays):
#   dic = {}
#   agg = {}
#   for i in range(len(genres)):
#     dic[plays[i]] = i
#     agg[plays[i]] = genres[i]
#   sortedAgg = sorted(agg, reverse=True))
#   visited = [False for _ in range(len(sortedAgg))]

#   i = 0
#   ans = []
#   for a in sortedAgg:
#     if visited[dic[a]] == True:
#       continue
#     pivot = agg[a]
#     appCnt = 0
#     for j in range(i, len(agg)):
#       if agg[sortedAgg[j]] == pivot:
#         visited[dic[sortedAgg[j]]] = True
#         ans.append(dic[sortedAgg[j]])
#         appCnt += 1
#     i+=1
#     if appCnt > 2:
#       for i in range(appCnt-2):
#         ans.pop()
#   return ans

# # 답: 4, 2, 3, 장르별로 2개임!!
# print(solution(['B', 'B', 'B', 'B', 'A'], [500, 150, 800, 800, 2500]))
