class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self, root=None):
        self.root = root

    def create_minimal_bst(self, array):
        self.root = self.minimal_bst(array, 0, len(array)-1)

    def minimal_bst(self, array, low: int, high: int):
        if high < low:
            return None
        mid = (low + high) // 2

        node = Node(array[mid])
        node.left = self.minimal_bst(array, low, mid - 1)
        node.right = self.minimal_bst(array, mid + 1, high)
        return node
    
    def search_node(self, target):
        current = self.root
        while current:
            if target == current.value:
                return True
            elif target < current.value:
                current = current.left
            else:
                current = current.right
        return False

if __name__ == "__main__":
    bst = BST()
    array = [1, 2, 3, 5, 7, 8]
    bst.create_minimal_bst(array)
    
    # Testing search functionality
    target = 5
    found = bst.search_node(target)
    print(f"Is {target} in the tree? {found}")

    target = 4
    found = bst.search_node(target)
    print(f"Is {target} in the tree? {found}")

