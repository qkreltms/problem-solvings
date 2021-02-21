'''
'''


def solution(begin, target, words):
    if target not in words:
        return 0

    def find(item):
        result = []
        # 이미 방문했던건 넣지 않는다.
        for word in list(filter(lambda x: visited[x] == 0, words)):
            cnt = 0
            for a, b in zip(item, word):
                if a != b:
                    cnt += 1
            if cnt == 1:
                result.append(word)
        return result

    visited = {key: False for key in [*words, begin]}
    queue = [(begin, 0)]
    while queue:
        q, cnt = queue.pop(0)
        if visited[q] == False:
            if q == target:
                return cnt
            visited[q] = True
            queue.extend((key, cnt+1) for key in find(q))


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]), 1)
print(solution("1234567000", "1234567899", [
      "1234567800", "1234567890", "1234567899"]), 3)
print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]), 4)
