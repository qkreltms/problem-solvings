#문제
'''
최대 힙 구현
입력:
첫 줄 = 연산의 개수 => k
두번째 줄 ~ k
0일 경우 루트 출력
n일 경우 값을 최대 힙에 넣음
'''
#내 실수
'''
1. 삭제시 자녀 둘 다 비교후 가장 작은/큰 값과 바꿔야 함
2. 삭제시 비교하는 부모 값이 newRoot로 고정적이었음...
'''

import sys
class MaxHeap:
    heap = [None]

    def __init__(self, src):
        # src는 숫자 배열이라고 가정한다.
        self.heap = [None]
        self.init(src)

    def __len__(self):
        return len(self.heap[1:])

    def init(self, src):
        for i in range(len(src)):
            self.heap.append(src[i])
            if i == 0:
                continue
            pi = (i+1) // 2
            ci = i+1
            while pi:
                if self.heap[pi] < self.heap[ci]:
                    temp = self.heap[pi]
                    self.heap[pi] = self.heap[ci]
                    self.heap[ci] = temp
                    ci = pi
                    pi //= 2
                else:
                    break

    def add(self, n):
        self.heap.append(n)
        if len(self.heap) > 1:
            pi = (len(self.heap)-1) // 2
            ci = (len(self.heap)-1)
            while pi:
                if self.heap[pi] < n:
                    temp = self.heap[pi]
                    self.heap[pi] = self.heap[ci]
                    self.heap[ci] = temp
                    ci = pi
                    pi //= 2
                else:
                    break

    def delete(self):
        # 빈 힙일 경우
        if len(self.heap) < 2:
            return 0
        oldRoot = self.heap[1]
        if len(self.heap) == 2:
            del self.heap[1]
            return oldRoot
        newRoot = self.heap.pop()
        self.heap[1] = newRoot

        pi = 1
        # 최소 왼쪽 노드는 있는지 확인
        while len(self.heap)-1 >= pi*2:
            lc = pi*2
            rc = lc + 1
            flag = 'l'
            lcv = self.heap[lc]
            if len(self.heap)-1 >= rc:
                rcv = self.heap[rc]
                if rcv > lcv :
                    flag = 'r'

            # 노드중 가장 작은 값과 바꿔준다.
            # 아래로 내려간다.
            if flag == 'l' and self.heap[lc] > self.heap[pi]:
                # 왼쪽 노드가 부모 위치로
                temp = self.heap[lc]
                self.heap[lc] = self.heap[pi]
                self.heap[pi] = temp
                pi = lc
                continue
            # 오른쪽 노드가 있는지 확인 후 비교
            elif flag == 'r' and self.heap[rc] > self.heap[pi]:
                temp = self.heap[rc]
                self.heap[rc] = self.heap[pi]
                self.heap[pi] = temp
                pi = rc
                continue
            return oldRoot
        return oldRoot

    def getHeap(self):
        return self.heap[1:]

    def getRoot(self):
        return self.heap[1]


k = int(sys.stdin.readline())
heap = MaxHeap([])
for _ in range(k):
    n = int(sys.stdin.readline())
    if n > 0:
        heap.add(n)
    if n == 0:
        print(heap.delete())

