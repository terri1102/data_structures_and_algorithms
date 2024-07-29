class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        # Insert the item at the end of the heap
        self.heap.append(item)
        # Move the new item to its correct place to maintain the heap property
        self._bubble_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # Swap the root with the last item and remove the last item (largest element)
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        # Move the new root to its correct place to maintain the heap property
        self._bubble_down(0)
        return root

    def search(self, item):
        # Simple linear search to find the item
        for index, value in enumerate(self.heap):
            if value == item:
                return index
        return -1

    def delete(self, item):
        index = self.search(item)
        if index == -1:
            return False

        # Move the item to delete to the end by replacing it with the last item
        self.heap[index] = self.heap[-1]
        self.heap.pop()
        # Restore the heap since the last item might be out of place
        if index < len(self.heap):
            self._bubble_up(index)
            self._bubble_down(index)
        return True

    def _bubble_up(self, index):
        while index > 0 and self.heap[index] > self.heap[(index - 1) // 2]:
            self.heap[index], self.heap[(index - 1) // 2] = (
                self.heap[(index - 1) // 2],
                self.heap[index],
            )
            index = (index - 1) // 2

    def _bubble_down(self, index):
        child_index = 2 * index + 1
        while child_index < len(self.heap):
            # Find the largest child to potentially swap with
            max_child_index = child_index
            if (
                child_index + 1 < len(self.heap)
                and self.heap[child_index + 1] > self.heap[child_index]
            ):
                max_child_index = child_index + 1

            if self.heap[index] >= self.heap[max_child_index]:
                break

            self.heap[index], self.heap[max_child_index] = (
                self.heap[max_child_index],
                self.heap[index],
            )
            index = max_child_index
            child_index = 2 * index + 1


# Example usage
if __name__ == "__main__":
    h = MaxHeap()
    h.insert(10)
    h.insert(4)
    h.insert(15)
    h.insert(20)
    h.insert(30)
    h.insert(5)

    print(
        "Extract Max:", h.extract_max()
    )  # Should print the largest element and remove it
    print("Current Max:", h.heap[0])  # Should print the new largest element

    print("Search for element 15:", h.search(15))  # Should return the index of 15

    h.delete(15)
    print("Heap after deleting 15:", h.heap)
