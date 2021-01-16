def solution(people, limit):
    answer = 0
    i, j = 0, len(people)-1
    people.sort()
    while j >= i:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        answer += 1
    return answer
