# 문제
'''
return 연산 처리후 큐가 비어있으면 [0, 0], 비어있지 않으면 [최댓값, 최솟값]
이중우선순위큐를 만든다.
최소값, 최대값을 얻을 수 있어야됨
I 숫자 => 삽입
D 1 => 큐에서 최댓값 삭제
D -1 => 큐에서최솟값 삭제

단, 큐가 비어있을 때 삭제 연산 => 무시
삭제 연산 일 때 최댓값 or 최솟값이 두개 라면 하나만 삭제.
'''
# 풀이법
'''
1트
추가되는 값들은 그냥 배열에 저장해 놓는다.
2. 만약, 최댓값을 삭제한다면 그 때 최대 heap을 만들어서(heapify) 하나 삭제한다.
3. 만약, 최솟값을 삭제한다면 그 떄 최소 heap을 만들어서 하나 삭제한다.
출력할 때 2, 3을 실행하는데 만약 배열이 비어있다면 0을 출력, 최댓값 우선(?)
=> heapify 가 log(n)

2트
값을 먼저 다 받은 후 그 값을
내림차순 정렬한 배열을(A) 하나 만든다
min heap을 하나 만든다.
visited = []
만약 최대값을 삭제한다면 A에서 pop(0) 해주고 visited에 넣어준다.
만약 최솟값을 삭제한다면 heap에서 pop()을 해주고 그 값이 visited 안에 있는지 확인한다.(for 문 쓰는게 빠를 듯)
만약 그 값이 visited에 있다면 flag 를 false로 주고 모든 데이터가 삭제됐다고 판단한다. => 다음 삭제시 둘 다 무조건 무시

3트
왜 힙을 써야되지???
명령어가 한번에 들어오니까, 다 받아서 다듬은 뒤,
그냥 정렬된 배열 하나 두고 앞, 뒤 가리키는 포인터 두고 자르면 되는거 아닌가?
=> 삭제 명령어가 사이사이마다 들어오는데, 3트 방법 대로면 좀 까다로워짐

4트 2트 방법 수정
1. max heap, min heap, 이 둘을 동기화 시켜줄 배열 A를 만든다.
2. 두 heap, A에 값을 잘 넣고, 삭제 명령어가 떨어지면 A에 값이 있는지 확인 후
값 삭제, A에 해당 값도 삭제 => max, min heap에 A에 없는 값이 계속 남아있어 영향을 줌

다만, 위 방법은 n2이 소요됨 heap을 삭제, 추가 해도 결국 nlogn정도 밖에 들지 않으니까
그냥 어떤 heap에 삭제가 일어나면 반대쪽 쪽힙에는 그 값을 찾을 때까지 pop한 후
그 값을 찾으면 그 값 삭제하고 나머지 값들은 다시 넣어주면 되지 않을까?
=> 아래 코드와 같이 위와 비슷하지만 좀 다른 식으로 풀었음, 다만 O(n2)이라 성능 걱정을 했지만 통과함 
'''




import heapq
def solution(ops):
    ops.append("D -1")
    ops.append("D 1")
    maxHeap = []
    minHeap = []
    A = []
    ans = [0, 0]
    for op in ops:
        # 추가
        if op[0] == "I":
            value = int(op[2:])
            heapq.heappush(maxHeap, -value)
            heapq.heappush(minHeap, value)
        # 삭제
        if op[0] == "D":
            # min heap 삭제
            if op[2] == '-':
                if minHeap:
                    minValue = heapq.heappop(minHeap)
                    maxHeap.pop(maxHeap.index(-minValue))
                    ans[1] = minValue
                else:
                    ans[1] = 0

            # max heap 삭제
            else:
                if maxHeap:
                    maxValue = heapq.heappop(maxHeap)
                    minHeap.pop(minHeap.index(-maxValue))
                    ans[0] = -maxValue
                else:
                    ans[0] = 0
    return ans


print(solution(["I 16", "D 1"]), [0, 0])
print(solution(["I 7", "I 5", "I -5", "D -1"]), [7, 5])
print(solution(["I -5"]), [0, -5])
print(solution(	["I 16", "I -5643", "D -1",
                 "D 1", "D 1", "I 123", "D -1"]), [0, 0])
print(solution(	["I -45", "I 653", "D 1", "I -642",
                 "I 45", "I 97", "D 1", "D -1", "I 333"]), [333, -45])
