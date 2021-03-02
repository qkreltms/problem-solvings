# 배운점
'''
sort 알고리즘 특성상 리스트를 헤집는게 아니기 때문에
넣은 그대로 인덱스가 들어간다.
'''


def solution(genres, plays):
    dic = {}
    idxs = [n for n in range(len(genres))]
    sumDic = {}
    for g, p, i in zip(genres, plays, idxs):
        if g in dic:
            dic[g].append((i, p))
            sumDic[g] += p
        else:
            dic[g] = [(i, p)]
            sumDic[g] = p

    ans = []
    for g, _ in sorted(sumDic.items(), key=lambda x: x[1], reverse=True):
        if dic[g]:
            sortedGenres = sorted(dic[g], key=lambda x: x[1], reverse=True)[0:2]
            ans.extend(sortedGenres)
    return [a[0] for a in ans]


# print(solution(['A', 'B', 'A', 'A', 'B'], [
#       500, 600, 150, 800, 2500]) == [4, 1, 3, 0])
# print(solution(['B', 'A'], [500, 600]) == [1, 0])
# print(solution(['B'], [500]) == [0])
# print(solution(['B', 'A'], [600, 500]) == [0, 1])
# print(solution(['A', 'B'], [600, 500]) == [0, 1])
# print(solution(['A', 'A', 'B'], [600, 500, 300]) == [0, 1, 2])
# print(solution(['A', 'B', 'A'], [600, 500, 600]) == [0, 2, 1])
# print(solution(['A', 'B', 'A'], [600, 500, 700]) == [2, 0, 1])
# print(solution(['A', 'A', 'A'], [600, 500, 700]) == [2, 0])
# print(solution(['A', 'A', 'A'], [3, 2, 1]) == [0, 1])
# print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],
#                [500, 600, 150, 800, 2500]) == [4, 1, 3, 0])
# print(solution(['classic'], [2500]) == [0])
# print(solution(['A', 'B', 'C'], [1, 2, 3]) == [2, 1, 0])
# print(solution(['A', 'B', 'C', 'D'], [1, 2, 3, 1]) == [2, 1, 0, 3])
# print(solution(['A', 'A', 'B', 'A'], [2, 2, 2, 3]) == [3, 0, 2])
# print(solution(['A', 'A', 'B', 'A'], [5, 5, 6, 5]) == [0, 1, 2])
print(solution(['A', 'A', 'B', 'A', 'B', 'B'], [5, 5, 6, 5, 7, 7]) == [4, 5, 0, 1])
