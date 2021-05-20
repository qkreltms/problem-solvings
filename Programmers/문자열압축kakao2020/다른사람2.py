# 2회차 로직과 원리를 동일하지만 훨씬더 간결화됨

def solution(s):
    answer = len(s)
    for x in range(1, int(len(s)/2)+1):
        d = 0
        comp = '' # 이전값저장
        c = 1
        for i in range(0, len(s), x):
            # n,...,3,2,1로 잘라준다
            temp = s[i:i+x]
            if comp == temp:
                c += 1
            # 처음에 comp가 빈 값이기 때문에 무조건 다를 수 밖에없다.
            # 다음 문자열이 현재랑 다르면
            elif comp != temp:
                # 문자열 길이 더함
                d += len(temp)
                if c > 1:
                    # 카운트 길이만 더함
                    d += len("{}".format(c))
                c = 1
                comp = temp
        # 만약 다음값이 같았다면 c만 더하다 끝났으므로 그 길이를 정답에 더해준다. 
        if c > 1:
            d += len("{}".format(c))
        answer = min(answer, d)
    return answer

print(solution('aaaa'))