'''
return 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는가?
트럭은 1초에 1만큼 움직인다.
무게 제한이 있다.
순차적으로
'''
from collections import deque 
def solution(BL, BW, TWs):
    WTs = deque(TWs)
    WLs = deque()
    time = 0
    while WTs or WLs:
      if len(WTs) > 0:
        wt = WTs[0]
        if sum(WLs) + wt <= BW and len(WLs) <= BL:
          WLs.append(wt)
          WTs.popleft()

      time += 1
      # 시간이 경과하면 차가 한 칸씩 이동하고 
      # 다리를 건너는 트럭해서 하나 제거함
      # 나누기(시간이 길이보다 일정수 커지면 x), 몫이(10이 넘어가면 작동 안됨)아닌 다른 로직 필요
      if time // BL == 1:
        WLs.popleft()
    return time
# print(solution(2, 10, [7,4,5,6]), 8)
# print(solution(100, 100, [10]), 101)
print(solution(100, 100, [10 for _ in range(10)]), 110)

    