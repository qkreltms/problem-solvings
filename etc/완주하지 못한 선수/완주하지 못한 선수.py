participant = ['leo', 'kiki', 'eden']
completion = 	['eden', 'kiki']

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]
         

solution(participant, completion)
# 배운 것 정렬을 하고 비교하면 빠르다

# Other's
######################
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
##############
# 해시 키를 더하고 뺀 후 남는 값이 완주하지 못 한 선수이다.
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer