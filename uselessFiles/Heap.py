from typing import List
from Node import Node 

class Heap:
    def __init__(self):
        self.heap: List['Node'] = []

    def push(self, item:Node):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("pop from an empty heap")
        
        self._swap(0, len(self.heap) - 1)
        smallest = self.heap.pop()
        self._heapify_down(0)
        return smallest

    def peek(self):
        if len(self.heap) == 0:
            raise IndexError("peek from an empty heap")
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index].state < self.heap[parent_index].state:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        smallest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < len(self.heap) and self.heap[left_child_index].state < self.heap[smallest].state:
            smallest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index].state < self.heap[smallest].state:
            smallest = right_child_index

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __str__(self):
        return str(self.heap)
