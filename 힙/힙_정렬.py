# 힙 (우선순위 큐에 사용)
'''
참고: https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html

1. 정의
완전 이진 트리(부모 1개에 자녀 2개, 노드는 왼쪽부터 채워짐)
최대 힙(부모 노드가 자식보다 큼), 최소 힙이 있음(낮음)
배열로 구현
부모, 자식 관계 =>
왼쪽 자식 = (부모의 인덱스 * 2)
오른쪽 자식 = (부모의 인덱스 * 2 + 1)
부모 = (자식의 인덱스) / 2

2. 삽입
배열의 가장 마지막에 넣음
그 후 부모 노드와 비교하며 정렬
3. 삭제
배열의 0번째 루트 노드 삭제
힙의 마지막 노드를 가져와 루트로 놓는다.
자식 노드와 비교하며 졍렬
'''

# TODO: 힙 알고리즘 틀린 듯함 관련 문제 풀어보기


class MinHeap:
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
                if self.heap[pi] > self.heap[ci]:
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
                if self.heap[pi] > n:
                    temp = self.heap[pi]
                    self.heap[pi] = self.heap[ci]
                    self.heap[ci] = temp
                    ci = pi
                    pi //= 2
                else:
                    break

    def delete(self):
        if len(self.heap) < 2:
            return None
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
                if lcv > rcv:
                    flag = 'r'

            # 노드중 가장 작은 값과 바꿔준다.
            if flag == 'l' and self.heap[lc] < newRoot:
                temp = self.heap[lc]
                self.heap[lc] = newRoot
                self.heap[pi] = temp
                pi *= 2
                continue
            # 오른쪽 노드가 있는지 확인 후 비교
            elif flag == 'r' and self.heap[rc] < newRoot:
                temp = self.heap[rc]
                self.heap[rc] = newRoot
                self.heap[pi] = temp
                pi *= 2 + 1
                continue
            return oldRoot
        return oldRoot

    def getHeap(self):
        return self.heap[1:]

    def getRoot(self):
        return self.heap[1]


# test
heap = MinHeap([])
heap.delete()
print(heap.getHeap(), [])
heap = MinHeap([1])
heap.delete()
print(heap.getHeap(), [])
heap = MinHeap([1, 2])
heap.delete()
print(heap.getHeap(), [2])
heap = MinHeap([1, 2, 5, 3, 9, 8, 6, 9, 7])
print(heap.getHeap(), [1, 2, 5, 3, 9, 8, 6, 9, 7])
heap = MinHeap([1, 2, 5, 3, 9, 8, 6, 9, 7])
heap.delete()
print(heap.getHeap(), [2, 3, 5, 7, 9, 8, 6, 9])
heap = MinHeap([1, 2, 5, 3, 9, 8, 6, 9, 7])
heap.delete()
heap.delete()
print(heap.getHeap(), [3, 7, 5, 9, 9, 8, 6])
heap = MinHeap([9, 8, 7, 6])
print(heap.getHeap(), [6, 7, 8, 9])

heap = MinHeap([1, 2, 3, 4, 5])
heap.add(0)
print(heap.getHeap(), [0, 2, 1, 4, 5, 3])
