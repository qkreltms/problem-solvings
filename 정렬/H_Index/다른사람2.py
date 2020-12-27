def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    print(list(enumerate(citations, start=1)))
    print(list(map(min, enumerate(citations, start=1))))

    return answer


print(solution([3, 0, 6, 1, 5]), 3)
