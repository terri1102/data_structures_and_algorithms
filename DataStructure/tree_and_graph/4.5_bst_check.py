class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
class BST:
    def __init__(self, root=None):
        self.root = root
    
    def traverse(self):
        stack = []
        root, temp = self.root, self.root
        
        if self.root is not None:
            while temp.left is not None:
                prev = temp
                temp = temp.left
                temp.parent = prev
            left_end = temp
            stack.append(left_end)
            while temp != root:
                stack.append(temp)
                stack.append(temp.parent)
                if temp.right is not None:
                    stack.append(temp.right)

                temp = temp.parent


        return stack
    def check_bst(self):
        result = self.traverse()
        if result == sorted(result):
            return True
        else:
            return False
        # 이진 탐색 트리의 특징 체크해야 함
                # 1. increasing order
