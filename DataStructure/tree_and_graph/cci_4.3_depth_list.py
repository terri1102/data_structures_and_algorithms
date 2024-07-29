# 이진트리가 주어졌을 때 같은 깊이에 있는 노드를 연결리스트로 연결해주는 알고리즘.
# 트리 깊이가 D라면 D개의 연결리스트 존재함
from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class LinkNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
    #class BinaryTree:
        #def __init__(self, root=None):
    #self.root = root

    #def create_linked_list(self, root, depth):

def list_of_depths(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        head = LinkNode(0) # 더미 노드
        current = head

        for _ in range(level_size):
            node = queue.popleft()
            current.next = LinkNode(node.value)
            current = current.next

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(head.next)

    return result

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=' -> ')
        current = current.next
    print("None")

# 예제 이진 트리 구성
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    lists = list_of_depths(root)
    for i, l in enumerate(lists):
        print(f"Level {i+1}: ", end="")
        print_linked_list(l)
