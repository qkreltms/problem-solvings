'''
'''
def solution(participants, completions):
    participants.sort()
    completions.sort()
    completions.append('')
    for p, c in zip(participants, completions):
        if p != c:
            return p
