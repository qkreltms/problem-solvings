# 문제
'''
'''
# 풀이 법
'''
1#
x, y값이 주어지면 그 두 값을 더한다.(x+y) = z
w:3, h:3 부터 시작
z 값을 w값으로 h 번 나눴을 때 값이 남았는지 확인한다.
남았다면
w:4, h3, 남았다면
w:4, h4, 남지 않았다면
결과값 리턴
반례: 24, 24
2#
(약수구하기)
x * y = z 일때 z에서 나올 수 있는 y가 가장 큰 x, y 값 출력
, 단 x >= y
예: z=48 일 때 (12,4), (8,6) 

=> 반례 존재
세로 길이와 같거나, 세로 길이보다긴 카펫이 여러개인데
이 때 어떤 값을 반환해야하는가?
'''




import math
def solution(x, y):
    z, h, w = x+y, 3, 3
    xyList = []
    root = math.ceil(z ** 0.5)
    while True:
        if z % h == 0:
            w = int(z//h)
            xyList.append((w, h))
        if h >= root:
            break
        h += 1
    # 갭이 젤 작은 값을 출력한다.

    ans = xyList[0]
    print(xyList)
    if ans[0] > ans[1]:
        return [ans[0], ans[1]]
    return [ans[1], ans[0]]


print(solution(10, 2), [4, 3])
print(solution(8, 1), [3, 3])
print(solution(24, 24), [8, 6])
print(solution(10, 2), [4, 3])
print(solution(14, 4), [6, 3])
print(solution(50, 22), [24, 3])
print(solution(18,12), [6,5])