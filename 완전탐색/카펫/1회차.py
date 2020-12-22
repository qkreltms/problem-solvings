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
x + y = z 일때 z에서 나올 수 있는 약수 계산
, 단 x >= y
예: z=48 일 때 (12,4), (8,6) 

=> 반례 존재
세로 길이와 같거나, 세로 길이보다긴 카펫이 여러개인데
이 때 어떤 값을 반환해야하는가? => 사각형 너비 공식 이용
w * h, 여기서 둘레를 감싸고있는 brown은 좌우 총 2칸, 위아래 총 2칸을 차지하므로 이 값을 빼면
Yellow의 값이 나온다. => (w-2)*(h-2) = Yellow

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

    for w, h in xyList:
        if ((w-2)*(h-2)) == y:
            return [w, h] 


print(solution(10, 2), [4, 3])
print(solution(8, 1), [3, 3])
print(solution(24, 24), [8, 6])
print(solution(10, 2), [4, 3])
print(solution(14, 4), [6, 3])
print(solution(50, 22), [24, 3])
print(solution(18,12), [6,5])