def solution(numbers):
    numbers = list(map(str, numbers))
    # 첫 글짜를 사전식 비교, 다르면 큰 순서가 큼, 같으면 그 다음것 비교
    # https://docs.python.org/2/tutorial/datastructures.html#comparing-sequences-and-other-types
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


print(solution([6, 10, 2]))
