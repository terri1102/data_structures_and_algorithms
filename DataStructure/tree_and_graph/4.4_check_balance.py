from collections import deque
class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right
    
    #def inorder_traverse(self):
        #queue = deque([self.value])
        #while queue:
        #    temp = queue.popleft()
        #    print(temp.value)
        #        if self.left:
        #        queue.append(self.left)
        #    if self.right:
    #        queue.append(self.right)

class BinaryTree:
    def __init__(self, root):
        self.root = root
    def inorder_traverse(self):
        if self.root is not None:
            self.inorder_traverse(self.root)
            print(self.root.value)

            
    def return_depth(self, node: Node):
        depth = 1
        queue = deque([[node, depth]])
        while queue:
            node, depth = queue.popleft()
            if (node.left is None) and (node.right is None): ################ if not node.left 로 체크하면 안 됨..! None 노드가 있는 셈이기에!!!!!!!!!1
                return depth
            elif node.left:
                queue.append([node.left, depth+1])
            elif node.right:
                queue.append([node.right, depth+1])
        return 0

def solution(tree: BinaryTree) -> bool:
    root = tree.root
    
    if (root.left is None) or (root.right is None):
        return True
           
    left_depth = tree.return_depth(root.left)
    right_depth = tree.return_depth(root.right)
    print(f"Left depth: {left_depth}, Right depth: {right_depth}")
    if -1 <= left_depth - right_depth <= 1:
        return True
    else:
        return False

if __name__ == "__main__":
    node = Node(2)
    node.left = Node(1)
    node.right = Node(3)
    node.left.left = Node(0)
    bt1 = BinaryTree(node)
    #print(node.inorder_traverse())
    print(solution(bt1))

    node2 = Node(5)
    node2.right = Node(7)
    node2.left = Node(3)
    node2.left.left = Node(2)
    node2.left.right = Node(4)
    node2.left.left.left = Node(1)
    node2.left.left.right = Node(2)
    bt2 = BinaryTree(node2)
    print(solution(bt2))
