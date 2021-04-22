'''
초 단위 주식가격 배열이 주어질 때
가격이 떨어지지 않은 기간은 몇 초인가?
'''
# 풀이법
'''
뒤부터 순회하며 그대로, 상승, 하락 장을 표시한다.
하락장인 것은 볼 것도없이 1이고
상승장은 거쳐갔던 배열을 순회하며 카운트를 진행해야한다.
'''
# 배운점
'''
안될것 같아도 해보자 n2 => n, n log n 으로 줄이는 것도 좋지만
n2이여도 루프 몇 번 더 줄이는 것으로 통과될 수 도있다.
'''


def solution(prices):
    l = len(prices)
    ans = [0 for _ in range(l)]
    upAndDowns = [0 for _ in range(l)]

    for i in range(l-2, -1, -1):
        if prices[i] <= prices[i+1]:
            upAndDowns[i] = 1
        else:
            upAndDowns[i] = -1

    l2 = len(upAndDowns)
    for i in range(l2-2, -1, -1):
        if upAndDowns[i] == -1:
            ans[i] = 1
        else:
            pivot = prices[i]
            cnt = 0
            for j in range(i+1, l):
                cnt += 1
                if pivot > prices[j]:
                    break
            ans[i] = cnt

    return ans


print(solution([1, 2, 3, 2, 3]))
