'''
'''


def solution(name):
    dic = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
           'N': 13, 'O': 12, 'P': 11, 'Q': 10, 'R': 9, 'S': 8, 'T': 7, 'U': 6, 'V': 5, 'W': 4, 'X': 3, 'Y': 2, 'Z': 1}

    ans = 0
    for s in name:
        ans += dic[s]

    l = len(name)
    cursor = l
    for i in range(l):
        if name[i] == 'A':
            continue

        next = i+1
        while next < l and name[next] == 'A':
            next += 1
        cursor = min(cursor, (i*2)+(l-next))
    ans += cursor
    return ans


print(solution("BBBAAABBAAABB"), 18)
print(solution("BBBAAAAABBB"), 13)
print(solution("ABBBBBAAAAAAABBBBB"), 25)
print(solution("ABBAAAAAB"), 8)
