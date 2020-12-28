def solution(name):
    cnt = 0  # 총 이동 횟수
    a_cnt = 0  # 'A'의 개수
    a_max = 0  # 'A'의 최대개수
    idx = 0  # 최대'A'개수 문자열의 마지막 인덱스
    a_startIdx = 0  # 최대'A'개수 문자열의 첫번째 인덱스
    wander_cnt = 0  # 좌우로 왔다갔다하는 횟수 카운트

    # 위, 아래 조이스틱 계산
    for i, n in enumerate(name):
        if n == 'A':  # 'A'개수의 최대값과 그 인덱스 계산
            a_cnt += 1
            if a_cnt > a_max:
                a_max = a_cnt
                idx = i
        else:
            cnt += min(ord(n)-ord('A'), ord('Z')-ord(n)+1)
            a_cnt = 0

    # 최대'A'개수의 시작 인덱스
    a_startIdx = idx-a_max + 1

    test = 0
    # 최대'A'가 맨 앞이나 맨 끝에 있는 경우
    if a_startIdx == 0 or idx == len(name) - 1:
        test = len(name)-1-a_max  # a_max개만큼 이동 안해도 됨
    else:
        left = len(name)-idx-1  # 최대'A'뒤에 남아있는 문자의 개수
        if a_startIdx <= left:  # 뒤에 문자가 앞에 문자개수보다 많은 경우
            wander_cnt = (a_startIdx-1)*2 + left
        else:
            wander_cnt = (a_startIdx-1) + left*2
        test = min(wander_cnt, len(name)-1)  # 그냥 한쪽방향으로 모두 이동하는 것과 비교
    print(test)
    return cnt + test


print(solution("BBBAAABBAAABB"), 18)
print(solution("BBBAAAAABBB"), 13)
print(solution("ABBBBBAAAAAAABBBBB"), 25)
