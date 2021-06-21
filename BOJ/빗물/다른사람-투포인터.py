# 문제: https://velog.io/@kynel/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B9%97%EB%AC%BC-%ED%8A%B8%EB%9E%98%ED%95%91
# 풀이 법:
'''
투 포인터 방식

가장 왼쪽, 오른쪽의 max 값을 찾는다.
그 후 왼쪽, 오른쪽 max 값을 비교하면서
만약 왼쪽이 같거나 작으면 오른쪽으로 1 이동
아니면 오른쪽이 1 이동
하면서 max-현재 값을 저장한다.
반복

증명:
1. max 값이 있다는 것은 벽이 있다는 것
2. 왼쪽 오른쪽 벽이있어야 빗물이 고이므로 범위를 왼,오른 max값을 찾으며 계산한다.
3. max 값을 계속 초기화 해주면서 중간에 max 값이 있어도 결과값은 0 (leftmax-heights[left]) 이 되도록하여 오답이
나오지 않게한다. volume+=0

'''
def rainTrap(heights):
    if not heights:  # 예외 처리
        return 0

    volume = 0
    left, right = 0, len(heights) - 1
    left_max, right_max = 0,0

    while left < right:
        left_max, right_max = max(heights[left], left_max), max(
            heights[right], right_max)

        if left_max <= right_max:  # 투 포인터가 이동하는 조건을 설정한다.
            volume += left_max - heights[left]
            left += 1
        else:
            volume += right_max - heights[right]
            right -= 1

    return volume

print(rainTrap([0,3,2,1,3]), 3)