def solution(numbers, target):
    answer = 0
    current_list = [numbers[0], -numbers[0]]

    for i in range(1, len(numbers)):
        next_number = numbers[i]
        next_list = []
        for num in current_list:
            next_list.append(num + next_number)
            next_list.append(num - next_number)

        current_list = next_list

    for num in current_list:
        if num == target:
            answer += 1
    return answer