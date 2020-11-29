'''
'''


def solution(progresses, speeds):
    answer = []
    # 현재 일
    time = 0
    count = 0
    while len(progresses) > 0:
        # 작업은 비동기적으로 수행하므로
        # 현재 일수와 speeds를 곱해주면 되고 이 값을 진행상황과 더하면 현재 얼마나 진행했는지 알 수 있다.
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            # 연속적으로 위 if문이 통과되지 못 하면 다음 작업은 아직 안끝났다는 말이므로 count가 1이상이면 결과에 추가해준다.
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

print(solution([93, 30, 55], [1, 30, 5]), [2, 1])
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]), [1, 3, 2])