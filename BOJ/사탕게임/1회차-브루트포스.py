#링크
'''
문제: https://www.acmicpc.net/problem/3085
참고: https://gdlovehush.tistory.com/300
'''
#풀이 법
'''
0~n까지 좌우 하나씩 바꿔보며 연속값 확인
0~n까지 상하 하나씩 바꿔보며 연속값 확인
굳이 인접한 부분만 바꾸지 않아도 됨

브루트포스 알고리즘에서는 무식해져야한다. => 바꾼 다음에 전체 행렬 탐색해 개수 세기
'''
#키포인트
'''
'''

n=int(input())
ans=0
h=[[] for _ in range(n)]
for i in range(n):
    h[i]=list(input())
def swap(i,a,flag):
    if flag:
        if h[i][a] == h[i+1][a]:
          return True
        temp=h[i][a]
        h[i][a]=h[i+1][a]
        h[i+1][a]=temp
        
    else:
        if h[i][a] == h[i][a+1]:
          return True
        temp=h[i][a]
        h[i][a]=h[i][a+1]
        h[i][a+1]=temp
def check(i,j,flag):
    global ans
    if swap(i,j,flag):
      return
    for k in range(n):
        cnt,w=1,''
        for l in range(n):
            if h[k][l]!=w:
                w=h[k][l]
                ans=max(ans,cnt)
                cnt=1
            else:
                cnt+=1
        ans=max(ans,cnt)
    for k in range(n):
        cnt,w=1,''
        for l in range(n):
            if h[l][k]!=w:
                w=h[l][k]
                ans=max(ans,cnt)
                cnt=1
            else:
                cnt+=1 
        ans=max(ans,cnt)
    swap(i,j,flag)
def f():
    for i in range(n):
        for j in range(n-1):
            check(i,j,False)
            check(j,i,True)
    return ans
print(f())