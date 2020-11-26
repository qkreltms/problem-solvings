# 문제:
'''
return 모든 트럭이 순차적으로 다리를 건너려면 최소 몇 초가 걸리는가?
다리에 무게 제한이 있다.
다리위에 무게가 되는한 트럭을 최대한 올려놓는다.
트럭은 1초에 1만큼 움직인다.=> 다리는 특정 시간이 지나면 트럭이가 비워져야한다
트럭은 중간중간에 비지않는다.
'''
# 내 실수:
'''
1. 트럭이 최대한 다리가 버티는 한 올라가야하고
시간이 지날 수록 다리를 빠져나와야 하는데 여기서 
시간이 오래걸렸다.

2. 성능 이슈 => 어찌할 바를 모르겠다.
'''
# 키 포인트:
'''
다리를 건너는 트럭 대기열(A)
일정 시간이 지나면 A에서 먼저 들어온 순대로 하나씩 제거한다.
그 동안 트럭이 다리에 들어올 수 없다면 0으로 채워서 시간을 때운다.

성능 이슈:
먼저 빅오를 본다. 어디가 성능이 소요되는지 보고 최적화 한다...
처음에는 A를 계속 sum해서 A에 트럭이 들어와도 되는지 확인했는데
그러지말고 변화가 있을 때만 sum을 해주면 속도가 빨라진다. 
'''
from collections import deque 
def solution(BL, BW, TWs):
    WTs = deque(TWs)
    WLs = deque()
    time = 0
    sumOfWLs = 0
    while WTs or WLs:
      if time >= BL:
        sumOfWLs -= WLs.popleft()
      if len(WTs) > 0:
        wt = WTs[0]
        if sumOfWLs + wt <= BW and len(WLs) <= BL:
          WLs.append(wt)
          WTs.popleft()
          sumOfWLs += wt
        else:
          WLs.append(0)
      time += 1
    return time
print(solution(2, 10, [7,4,5,6]), 8)
print(solution(100, 100, [10]), 101)
print(solution(100, 100, [10 for _ in range(10)]), 110)
print(solution(10000, 10000, [10 for _ in range(10)]), 110)

    