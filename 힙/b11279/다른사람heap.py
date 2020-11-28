class min_heap(object):
    def __init__(self):
        self.queue = []

    def insert(self, n):
        self.queue.append(n)
        last_index = len(self.queue) - 1

        while 0 <= last_index:
            parent_index = self.parent(last_index)
            if 0 <= parent_index and self.queue[parent_index] < self.queue[last_index]:
                self.swap(last_index, parent_index)
                last_index = parent_index
            else:
                break

    def delete(self):
        last_index = len(self.queue) - 1
        if last_index < 0:
            return 0
        self.swap(0, last_index)
        minv = self.queue.pop()
        self.min_heapify(0)
        return minv

    def min_heapify(self, i):
        left_index = self.leftchild(i)
        right_index = self.rightchild(i)
        min_index = i

        if left_index <= len(self.queue) - 1 and self.queue[min_index] < self.queue[left_index]:
            min_index = left_index

        if right_index <= len(self.queue) - 1 and self.queue[min_index] < self.queue[right_index]:
            min_index = right_index

        if min_index != i:
            self.swap(i, min_index)
            self.min_heapify(min_index)

    def swap(self, i, parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]

    def parent(self, index):
        return (index - 1) // 2

    def leftchild(self, index):
        return index * 2 + 1

    def rightchild(self, index):
        return index * 2 + 2

import sys

n = int(sys.stdin.readline())
minheap = min_heap()
for i in range(n):
    command = int(sys.stdin.readline())
    if command == 0:
        print(minheap.delete())
    else:
        minheap.insert(command)