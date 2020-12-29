# 문제
'''
처음에 글자 수 대로 A로 셋팅되어있을 때
▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
return 위의 조작을 이용해 최소 조작 횟수 값
'''
# 키 포인트
'''
1. 상하 횟수 구하는 것은 dic에 키를 알파벳, 값을 횟수로 저장한다. 값은 A에서 몇 번 위,아래 이동횟수

2.
ABBBBBAAAAAAABBBBB
그냥 쭉 갔을 때 17
처음 A보자마자 뒤로 갔을 때 17
두 번째 A집합 보고 뒤로 갔을 때 15
루프를 돌면서 A가 아닌 알파벳이 나올 때 마다 뒤로 도는 횟수를 구하고 최솟값을 구한다.
예: BBBAAABBAAABB가 있을 때
첫 번째 B에서 바로 왼쪽으로 가면 처음 시작에서 오른쪽으로 이동 횟수 0, 왼쪽으로 이동 횟수 0, 젤 뒤로가서 처음위치 전까지 12번 총 12번을 이동한다.
두번째 B에서 똑같이하면 처음에서 오른쪽 이동 1, 왼쪽 이동 1, 젤 뒤로가서 처음위치 전까지 11번 총 13번 이동한다.
세번째 B에서는 다음 A의 개수를 구한다 총 3개 왜냐면 그만큼은 커서를 이동할 필요가 없으므로 처음에서 오른쪽이동 2번, 왼쪽이동 2번, 젤 뒤로가서 처음위치 전까지 총 10번 이동한다
식을 세워보면 r+l+len(A)-1-r(or l)-next, 여기서 r,l은 index로 대체 가능하다 정리하면 i*2+len(A)-1-i-next
'''


def solution(name):
    dic = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
           'N': 13, 'O': 12, 'P': 11, 'Q': 10, 'R': 9, 'S': 8, 'T': 7, 'U': 6, 'V': 5, 'W': 4, 'X': 3, 'Y': 2, 'Z': 1}

    ans = 0
    for s in name:
        ans += dic[s]

    l = len(name)-1
    cursorCnt = l
    for i in range(len(name)):
        if name[i] == 'A':
            continue
        next = 0
        while next+1+i < len(name) and name[next+1+i] == 'A':
            next += 1
        aCnt = next
        cursorCnt = min(cursorCnt, (i*2)+(l-i)-aCnt)
    ans += cursorCnt
    return ans


print(solution("BBBAAABBAAABB"), 18)
print(solution("BBBAAAAABBB"), 13)
print(solution("ABBBBBAAAAAAABBBBB"), 25)
print(solution("ABBAAAAAB"), 8)
