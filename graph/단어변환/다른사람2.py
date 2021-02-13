def solution(begin, target, words):
    answer = 0
    Q = [begin]

    while True:
        temp_Q = []
        for word_1 in Q:
            if word_1 == target:
                    return answer
            for i in range(len(words)-1, -1, -1):
                word_2 = words[i]
                if sum([x!=y for x, y in zip(word_1, word_2)]) == 1:
                    temp_Q.append(words.pop(i))

        if not temp_Q:
            return 0
        Q = temp_Q
        answer += 1