from collections import defaultdict

def nextWord(cur, words):
    ret = []
    for word in words:
        cnt = 0
        for idx in range(len(word)):
            if word[idx] == cur[idx]:
                cnt += 1
        if cnt == len(cur)-1:
            ret.append(word)
    return ret

def bfs(begin, target, words):
    visited = defaultdict(lambda: False)
    queue = nextWord(begin, words)
    count = 0
    min = 1e9

    while(len(queue) > 0):
        size = len(queue)
        count += 1

        for _ in range(size):
            key = queue.pop(0)
            visited[key] = True
            if (key == target and count < min):
                min = count
            for candidate in nextWord(key, words):
                if (visited[candidate] == False):
                    queue.append(candidate)

    if min == 1e9:
        return 0
    else:
        return min

def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer