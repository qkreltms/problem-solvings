# 주의 python 3.8 이상은 sort 알고리즘 바뀐듯
# x
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]

print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))

    