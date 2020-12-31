# 문제
'''
return 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 수
'''
# 키포인트
'''
예제의 알고리즘은 앞에서 부터 시작해 한칸 씩 이동하며 조합을 만들어준다.
예를 들어 92는 되도, 29는 없다.
이를 곰곰히 생각해보면
모든 조합을 구할 필요가 없다.
'''
# 풀이법
'''
1트: 모든 조합을 구해서 가장 큰수를 출력한다 => 시간 초과

2트:
예제의 알고리즘은 앞에서 부터 시작해 한칸 씩 이동하며 조합을 만들어준다.
예를 들어 92는 되도, 29는 없다.
이를 곰곰히 생각해보면
모든 조합을 구할 필요가 없다.
길이(l)가 10인 숫자에서 k개의 숫자를 제거하면 6개의 길이(l-k)를 가진 가장큰 조합이 나와야 한다.
처음에 숫자를 하나 고를때는 뒤에 5개를 무조건 남긴 상태에서 앞에서 그 범위를 제외한 범위에서 가장 큰수를 고른다.
예: 4177252841 이면, 52841을 제외하고 앞에서 부터 가장큰 수 7선택(2번째 인덱스) 
그 다음 수는 l-(r-1) 범위를 제외한 범위에서 가장 큰 수를 골라준다. 단, 이전 선택 값을 포함 하지 않는 범위
예: 2841 범위를 제외하고 725범위에서 가장 큰 수를 고른다. => 7(0번째 인덱스)
반복한다.
그러다가 이전에 선택한 가장 큰 값의 인덱스가 제외해야하는 범위의 시작을 가리키는 인덱스와
같아지면 남은 값은 모조리 결과값에 추가한다.
=> 775841

틀림 => 반례: solution("00100", 2), "100"), solution("77413258", 2), "774358") 하나는 s,e index가 끝을 가리키기전에 ans 길이 초과, 다른 하나는 둘 다 끝을 가리킬 때
시간 초과 => max가 1번만 돌아도 은근히 시간 소요가 많다. n횟수 가진것은 한번 돌더라도 피하라!
number max구할 때 주어진 조건에서 젤 높은 수 예: 9 가 나오면 뒤에 나오는 것은 볼 필요도 없다.
'''
# 1트, 정답은 나오지만 시간초과
# from itertools import combinations
# def solution(number, k):
#     return max(list(map(lambda x: ''.join(x), combinations(number, len(number)-k))))


def solution(number, k):
    l = len(number)
    rangeStartIdx = 0
    ansLen = l-k
    rangeEndIdx = k
    ans = ''
    for i in range(1, l+1):
        pick = ('0', 0)
        for j, s in enumerate(number[rangeStartIdx:rangeEndIdx+1], start=1):
            if pick[0] < s:
                pick = (s, j)
            # 꼼수, 9가 가장 높으니까 이것을 발견하면 나머지는 볼 필요도 없음
            if pick[0] == '9':
                break
        ans += pick[0]
        rangeStartIdx += pick[1]
        rangeEndIdx = (l-(ansLen-i))

        if len(ans) >= ansLen:
            break
        if rangeEndIdx >= l-1:
            rangeEndIdx = l-1
        if rangeStartIdx >= l-1:
            ans += number[rangeStartIdx:]
            break
    return ans


print(solution("1924", 2), "94")
print(solution("1231234", 3), "3234")
print(solution("4177252841", 4), "775841")
print(solution("4177252841", 4), "775841")
print(solution("1", 0), "1")

print(solution("87654321", 3), "87654")
print(solution("18765432", 3), "87654")
print(solution("77413258", 2), "774358")
print(solution("12345678901234567890", 19), "9")

print(solution("01010", 3), "11")
print(solution("559913", 1), "59913")
print(solution("9191919", 1), "991919")
print(solution("00100", 2), "100")
