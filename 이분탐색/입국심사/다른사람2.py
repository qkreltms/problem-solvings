'''
https://minnnne.tistory.com/32
'''
def binarySearch(left, right, times, n):
    cnt=0
    answer = -1
    while left <= right:
        mid = int((left+right)/2)
        cnt = 0
        for time in times:
            cnt += int(mid/time)

        if cnt >= n: 
            if answer == -1:
                answer = mid
            else:
                answer = min(answer,mid)
            right = mid-1
        elif cnt < n: left = mid+1
            
    return answer

def solution(n, times):
    times.sort()
    left = 0
    right = times[-1]*n
    answer = binarySearch(left, right, times, n)
    print(answer)
    return answer

solution(6,[7,10])