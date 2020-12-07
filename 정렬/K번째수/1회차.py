def solution(array, commands):
    ans = []
    for c in commands:
        a = array[c[0]-1:c[1]]
        a.sort()
        ans.append(a[c[2]-1])
    return ans
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]), [5,6,3])