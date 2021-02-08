# 문제
'''
https://www.acmicpc.net/problem/2839
설탕을 3, 5킬로 담을 수 있는 봉지가 있을 때 n이 주어진다면 
이것을 담을 수 있는 최소 봉지 갯수는?
'''
# 풀이법
'''
BFS 방식으로 품, 단 2^n이므로 중복되는 수는 set으로 없애줌
루프는 n / 가장 작은수+1 까지만
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


# print(f(5), 1)
# print(f(9), 3)
# print(f(3), 1)
# print(f(6), 2)
# print(f(18), 4)
# print(f(11), 3)
# print(f(4), -1)
