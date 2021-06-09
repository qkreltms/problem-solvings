
s = int(input())

start = 1;
end = s

while start <= end:
    mid = (start + end) // 2
    t=mid * (mid + 1) // 2
    if mid * (mid + 1) // 2 <= s:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)