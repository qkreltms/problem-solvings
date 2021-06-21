#링크
'''
문제: https://www.acmicpc.net/problem/14719


참고:
'''
#풀이 법
'''
벽을 담은 2차원 배열을 그리고
순회하며 
왼쪽 벽을 찾으면 flag=True 
벽이 아닌 부분을 찾으면 x+=1 
이 때 이전에 벽이 없었다면 다시 0으로 초기화
계속 +=1 하다가 오른쪽 벽을 만났으면 ans+=x 
'''
#키포인트
'''
반례를 더 다양하게 생각해보자
왼쪽 한칸이 다 비어있을 경우의 반례를 생각하기까지 오래걸림

문제를 좀 더 꼼꼼하게 읽자
"중간이 비는 경우는 존재하지 않는다."
'''


def f(w, h, m):
    if w <= 2:
        return 0
    ans = 0
    for i in range(h-1, -1, -1):
        x, flag = 0, False
        for j in range(w):
            if m[i][j]:
                x += 1
                if flag:
                    if j+1 < w and m[i][j+1] == False:
                        ans += x
                        x = 0
                else:
                    x = 0
            else:
                flag = True
    return ans


h, w = list(map(int, input().split(' ')))
walls = list(map(int, input().split(' ')))
m = [[True for _ in range(w)] for _ in range(h)]
for i in range(w):
    for j in range(h-1, h-1-walls[i], -1):
        m[j][i] = False
print(f(w, h, m))
