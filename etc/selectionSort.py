# 배열을 순회하며, a, b(a보다 위의 인덱스를 가진 값) 중 어떤 값이 높은지 또는 낮은지를 비교해 swap해 정렬한다.
def f(arr):
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
        print(arr)
    return arr


f([3,2,4,1,5])
