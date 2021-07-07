def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append('')
    for p,c in zip(participant, completion):
        if p!=c:
            return p
    