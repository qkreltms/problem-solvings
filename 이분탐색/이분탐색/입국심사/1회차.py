# 문제
'''
입국심사를 진행한다.
심사관마다 심사 시간이 다르다.
줄 하나가 있다.
처음에는 줄이 비어있다.
한 심사대에서는 한 명만 심사 가능하다.
줄의 가장 앞에 서 있는 사람은 비어있는 심사대로 이동 가능하다.
하지만 더 빠른 심사관이 있으면 기다렸다가 간다.

모든 사람이 심사 받는데 걸리는 최소 시간은?
'''
# 풀이방법
'''
심사관이 처리가능한 최소, 최대 범위를 구하고
대략 중간 값으로 심사관 모두의 처리량을 구한다.
만약 처리량이 n보다 낮으면
start 를 중간+1으로 옮기고 다시 한다.(작업량을 더 부여한다.) (loop)
만약 처리량이 n보다 높거나 같으면
end를 mid-1로 두어 작업을 계속한다.(최적 값을 찾기위해 작업량을 줄여본다.)
이렇게 작업량을 조절하며 범위를 좁히다보면 결과가 나온다.
만약 start <= end가 되면 작업을 종료하고 처리 결과를 반환한다. 
'''


def solution(n, times):
    fastestTime = min(times)
    start = fastestTime
    end = fastestTime*n

    ans = []
    while start <= end:
      mid = (start+end)//2
      sumTasks = 0
      for t in times:
        sumTasks += mid//t
        if n <= sumTasks:
          end = mid-1
          ans.append(mid)
          break
      if n > sumTasks:
        start = mid+1
    return min(ans)
  
print(solution(6, [7,10]), 28)
print(solution(1, [1]), 1)
print(solution(3, [1, 2]), 2)