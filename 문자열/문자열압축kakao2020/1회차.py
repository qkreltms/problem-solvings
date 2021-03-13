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
// 배열 자르기보다 result를 수정하는 식으로 해야할듯...
//
//
문자열 S가 주어지면
L = S[0:len(S)//2+2]
R = S[len(S)//2+1:]
result = S
while R:
    if L is empty:
        L = R[0:len(R)//2+1]
        R = R[len(R)//2:]
    else: 
        R.append(L.pop())

    if L[0] == R[0]:
        makeTable()
return len(result)

def makeTable():
    KMP 테이블 만드는 함수 변경해 이용
    cnt = 1
    숫자가 연속되는 만큼 카운트를 세주고 그 만큼 압축한다.(cnt+=1) 단, 연속되지 않으면 바로 break
    if cnt >= 2:
        L = []
        R = 연속되는 문자열 길이 제거한다.
'''
