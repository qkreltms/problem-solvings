# 문제
'''
https://www.acmicpc.net/problem/2839
설탕을 3, 5킬로 담을 수 있는 봉지가 있을 때 n이 주어진다면 
이것을 담을 수 있는 최소 봉지 갯수는?
'''
# 풀이법
'''
모든 경우의 수를 다 구해서 가장 먼저 0이 될 때 그 횟수를 반환한다.
'''

# 배운 점
'''
내가 너무 어렵게 생각하려고 할 때 생각을 
멈추고 다른 깔끔한 방식으로 생각해보자(다른사람1 참고)
'''

def f():
    n = int(input())
    queue = [n]
    ans = 0
    cnt = n//3+1
    while cnt:
        s = set()
        for _ in range(len(queue)):
            q = queue.pop(0)
            if q == 0:
                print(ans)
                return
                # return ans
            s.add(q-3)
            s.add(q-5)
        queue = list(s)
        ans += 1
        cnt -= 1
    print(-1)
    # return -1
f()

# print(f(7), -1)
# print(f(5), 1)
# print(f(9), 3)
# print(f(3), 1)
# print(f(6), 2)
# print(f(18), 4)
# print(f(11), 3)
# print(f(4), -1)
