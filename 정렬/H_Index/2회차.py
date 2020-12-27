def solution(citations):
    l = len(citations)
    ans = []
    for pick in range(1, l+1):
        cnt = 0
        for c in citations:
            if c >= pick:
                cnt += 1
            if cnt >= pick:
                ans.append(pick)
                break
    if not ans:
        return 0
    return max(ans)


print(solution([3, 0, 6, 1, 5]), 3)
print(solution([0, 0, 0, 0, 0]), 0)
print(solution([0, 0, 0, 0, 2, 3]), 2)
print(solution([0, 0, 0, 3, 5, 5, 6, 7, 7, 8]), 5)
print(solution([350, 452, 877]), 3)
