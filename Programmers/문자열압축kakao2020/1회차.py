# 문제
'''
문제: https://programmers.co.kr/learn/courses/30/lessons/60057

aabbaccc
2a2ba3c => 7

ababcdcdababcdcd
2ababcdcd

abc abc dede

abcabc abcabc dedede dedede
'''
# 풀이법
'''
1. ..., S//2개수 만큼 앞에서부터 묶어 최적화한 값을 results에 넣고 최소 len 값을 반환한다.
2. token화 시켜서 진행한다.(앞에서부터 n개, ..., n+1개씩 자른다.) string index에 접근해서 다루기 까다로움
'''


def solution(S):
    ans = len(S)
    for r in range(1, len(S)//2+1):
        tokens = []
        T, i = S, 0
        while T:
            tokens.append([T[0:r]])
            T = T[r:]
            i += 1
        tokens.append('!')  # end

        result = ''
        cur = 0
        while cur < len(tokens)-1:
            next = cur+1
            cnt = 1
            while tokens[cur] == tokens[next]:
                next += 1
                cnt += 1
            else:
                if cnt >= 2:
                    result += f'{cnt}{tokens[cur][0]}'
                else:
                    result += tokens[cur][0]
                cur = next
        ans = min(ans, len(result))
    return ans


print(solution('aabbcc'), 6)
print(solution('aabbaccc'), 7)
print(solution('ababcdcdababcdcd'), 9)
print(solution('abcabcdede'), 8)
print(solution('abcabcabcabcdededededede'), 14)
print(solution('xababcdcdababcdcd'), 17)
