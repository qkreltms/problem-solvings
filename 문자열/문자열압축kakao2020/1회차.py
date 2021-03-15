# 문제
'''
aabbaccc
2a2ba3c => 7

ababcdcdababcdcd
2ababcdcd

abc abc dede

abcabc abcabc dedede dedede
'''
# 풀이법
'''
1, ..., S//2개수 만큼 앞에서부터 묶어 최적화한 값을 results에 넣고 최소 len 값을 반환한다.
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
        while i > len(tokens):
            j = i+1
            cnt = 1
            while tokens[i] == tokens[j]:
                j += 1
                cnt += 1
            else:
                if cnt > 2:
                    result += str(cnt) + tokens[i]
                    i = j
                else:
                    result += tokens[i]
        ans = min(ans, len(result))
    return ans


print(solution('aabbcc'))
