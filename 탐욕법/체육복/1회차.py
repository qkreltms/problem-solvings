#문제
'''
전체 학생수 n, 체육복 도난 학생리스트 lost, 여벌 체육복 가져온 학생리스트 reserve가 주어질 때
여벌 체육복 가져온 학생이 바로 앞, 뒤 번호 학생에게 체육복을 줄 수 있다, 단 여벌 체육복 가져온 학생이
도난시 자기가 입음
return 체육복이 있는 최대 학생수

전체 학생의 수는 2명 이상 30명 이하입니다.
체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
* 중요: 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
'''
#키 포인트
'''
여벌 체육복 가져온 학생이
도난시 자기가 입음
'''
#내 실수
'''
문제를 잘 읽자: 
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 
이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 
남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

즉, 여벌 체육복이 있는 학생이 도난 당하면 자기가 입는다. 
그렇기 때문에 빌려주기전 자기가 입는 로직이 구현되어야 한다.(그리디)
'''

from copy import deepcopy 
def solution(n, lost, reserve):
    students = []
    for i in range(1,n+1):
        students.append(i)
    for i in lost:
        students[i-1] = 0
    # 도난 당한 사람이 여벌이 있을경우 그걸 쓰는것을 더 높은 우선순위로 처리한다.
    temp = deepcopy(reserve)
    for i in temp:
        if not students[i-1]:
            students[i-1] = i
            reserve.remove(i)

    for i in reserve:
        if i-2 >= 0:
            if not students[i-2]:
                students[i-2] = i
                continue
        if i < len(students):
            if not students[i]:
                students[i] = i
                continue
    ans = 0
    for i in students:
        if i > 0:
            ans += 1
    return ans

print(solution(5, [2,4], [1,3,5]), 5)
print(solution(5, [2,4], [3]), 4)
print(solution(3, [3], [1]), 2)
print(solution(2, [1], [1]), 2)
print(solution(2, [1], [2]), 2)
print(solution(2, [1,2], [1,2]), 2)
print(solution(5, [2,3], [1,2]), 4)
print(solution(5, [1,2,3,4,5], [1,2,3,4,5]), 5)
print(solution(5, [1], [5]), 4)

        