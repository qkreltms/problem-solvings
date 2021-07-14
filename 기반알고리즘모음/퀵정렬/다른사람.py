#링크
'''
문제:
참고:
'''
#풀이 법
'''
'''
#키포인트
'''
최선 시간복잡도 O(n log n)
평균 시간복잡도 O(n log n)
최악 시간복잡도 O(n^2)
'''

def quicksort(x):
    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return quicksort(less) + equal + quicksort(more)
print(quicksort([6,5,4,1,32,4,2,4]))