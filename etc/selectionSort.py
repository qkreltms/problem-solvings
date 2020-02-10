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
