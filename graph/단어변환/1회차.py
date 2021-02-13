# 문제
'''
단어 begin, target이 주어질 때 주어진 단어 배열에서 알파벳 하나씩만
바꿔서 target으로 변환할 때 최소 값은?

제한사항
한 번에 한 개의 알파벳만 바꿀 수 있습니다.
words에 있는 단어로만 변환할 수 있습니다.
각 단어는 알파벳 소문자로만 이루어져 있습니다.
각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
begin과 target은 같지 않습니다.
변환할 수 없는 경우에는 0를 return 합니다.
'''
# 배운 점
'''
예제에 나와있는 방법 말고 다른 방법이 있을 수 있다는 것을 알아야한다.
예를 들어
hit -> hot -> dot -> dog -> cog 의 방법도 있지만
hit -> hot -> lot -> log -> cog 의 방법도 있다.
'''
# 풀이 법
'''
#1
target이 단어배열에 포함됐는지 확인한다. 없으면 0 반환
begin이 주어지면 단어 하나만 바꿨을 때 일치하는 것을 배열 A에 넣는다.
A 배열을 pop(0)하면서 BFS알고리즘으로 과정을 반복하며 변환하면서 
target 찾는다.
최소값을 반환한다.
만약 못 찾으면 0 반환 
'''


def find(myString, strings):
    begin = [ord(c) for c in myString]
    while strings:
        s = strings.pop(0)
        target = [ord(c) for c in s]
        l = len(s)-1
        cnt = 0
        for i, t in enumerate(target):
            if begin[i] == t:
                cnt += 1
        if cnt == l:
            queue.append([s, visited[myString][0]])


def solution(begin, target, words):
    if target not in words:
        return 0
    global queue
    global visited
    queue = []
    words.append(begin)
    visited = {key: [0, i] for i, key in enumerate(words)}
    find(begin, words[0:])
    while queue:
        key, num = queue.pop(0)
        if visited[key][0] == 0:
            visited[key][0] = num+1
            if key == target:
                return visited[key][0]
            find(key, words[visited[key][1]+1:])
    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
print(solution("hit", "cog", ["hot","dot","dog","lot","log"]), 0)
print(solution("hit", "hot", ["hot","dot","dog","lot","log"]), 1)
print(solution("1234567000", "1234567899", ["1234567800", "1234567890", "1234567899"]), 3)
print(solution("hit", "cog", ["cog", "log", "log", "dog", "hot"]), 4)
