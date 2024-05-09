class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # swap the root with the last item and remove
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        # move the new root to its correct place to maintain the heap @property
        self._bubble_down(0)
        return root

    def search(self, item):
        for index, value in enumerate(self.heap):
            if value == item:
                return index
        return -1

    def delete(self, item):
        index = self.search(item)
        if index == -1:
            return False

        self.heap[index] = self.heap[-1]
        self.heap.pop()

        if index < len(self.heap):
            self._bubble_up(index)
            self._bubble_down(index)
        return True

    def _bubble_up(self, index):
        while index > 0 and self.heap[index] < self.heap[(index - 1) // 2]:
            self.heap[index], self.heap[(index - 1) // 2] = (
                self.heap[(index - 1) // 2],
                self.heap[index],
            )
            index = (index - 1) // 2

    def _bubble_down(self, index):
        child_index = 2 * index + 1
        while child_index < len(self.heap):
            min_child_index = child_index
            if (
                child_index + 1 < len(self.heap)
                and self.heap[child_index + 1] < self.heap[child_index]
            ):
                min_child_index = child_index + 1

            if self.heap[index] <= self.heap[min_child_index]:
                break
            self.heap[index], self.heap[min_child_index] = (
                self.heap[min_child_index],
                self.heap[index],
            )
            index = min_child_index
            child_index = 2 * index + 1


if __name__ == "__main__":
    h = MinHeap()
    h.insert(10)
    h.insert(4)
    h.insert(15)
    h.insert(20)
    h.insert(30)
    h.insert(5)
    print("Extract min", h.extract_min())
    print("Current min", h.heap[0])
    print("Search for element 15:", h.search(15))  # Should return the index of 15

    h.delete(15)
    print("Heap after deleting 15:", h.heap)
