#링크
'''
문제: https://www.acmicpc.net/problem/1700
'''
#풀이 법
'''
1. 멀티탭이 비어있으면 플러그를 꽂는다.
2. 이미 플러그가 멀티탭에 꽂혀있다면 무시
3. 비어있지 않다면 
3.1 멀티탭에서 꽂을 플러그 리스트의 젤 앞에 값 우선
3.2 멀티탭에 이미 꽂혀있는 플러그가 꽂을 플러그 리스트에 없다면 그 값 선택
3.3 swap 해준다. 
'''
#키포인트
'''
반례:
3 9
1 1 1 1 1 3 4 9 1
'''

n, k = list(map(int, input().split()))
nexts = list(map(int, input().split()))
if n >= k:
    print(0)
    exit(0)
curs=[0 for _ in range(n)]
def f():
    ans=0
    for i, d in enumerate(nexts):
        if d in curs:
            continue
        if 0 in curs:
          curs[curs.index(0)]=d
          continue
        maxLi, si = 0, 0
        for j, c in enumerate(curs):
            try:
                fi = nexts[i:].index(c)
                if fi > maxLi:
                    si = j
                    maxLi = fi
            except:
                si = j
                break
        curs[si] = d
        ans += 1
    return ans
print(f())
