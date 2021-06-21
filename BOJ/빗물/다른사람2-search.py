# 링크: https://jjangsungwon.tistory.com/121
# 참조: https://hwan-shell.tistory.com/276
if __name__ == "__main__":
    h, w = map(int, input().split())
    height = list(map(int, input().split()))

    area = 0
    for i in range(1, w - 1):
        # 현재 위치의 왼쪽 블록 중 가장 큰 높이를 찾는다.
        left_height = height[i]
        for j in range(i - 1, -1, -1):
            if left_height < height[j]:
                left_height = height[j]
        # 현재 위치의 오른쪽 블록 중 가장 큰 높이를 찾는다.
        right_height = height[i]
        for j in range(i + 1, w):
            if right_height < height[j]:
                right_height = height[j]
        # 왼쪽, 오른쪽 높이 중 작은 높이에서 현재 높이를 뺀 값을 더한다.
        final_height = min(left_height, right_height)
        area += final_height - height[i]

    print(area)

# 숏코딩 버전
H,W=map(int,input().split())
L=list(map(int,input().split()))
T=0
for i in range(W):
    T+=(min(max(L[:(i+1)]),max(L[i:]))-L[i])
print(T)