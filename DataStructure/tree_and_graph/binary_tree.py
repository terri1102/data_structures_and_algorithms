class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self._root = None
        self.__test_root = 12
        print(self.__test_root)
    def insert(self, data, method='iterative'):
        if method == 'recursion':
            self._root = self._insert_rec(self._root, data)
        else:
            self._insert_iter(data)

    def _insert_rec(self, node, data):
        if not node:
            node = Node(data)
        else:
            if node.data > data:
                node.left = self._insert_rec(node.left, data)
            else:
                node.right = self._insert_rec(node.right, data)
        return node

    def _insert_iter(self, data):
        if self._root is None:
            self._root = Node(data)
            return
        new_node = Node(data)

        curr = self._root
        parent = None

        while (curr != None):
            parent = curr
            if curr.data > data:
                curr = curr.left
            else:
                curr = curr.right
        if parent.data > data:
            parent.left = new_node
        else:
            parent.right = new_node
    
    def find(self, data):
        return self._find_data(self._root, data)

    def _find_data(self, node, data):
        if node is None:
            return False
        elif node.data == data:
            return True
        elif node.data > data:
            return _find_data(node.left, data)
        else:
            return _find_data(node.right, data)

    def delete(self, data):
        self._delete_data(self._root, data)
    
    def find_min_node(self, node):
        while node.left:
            node = node.left
        return node
    
    def _delete_data(self, node, data):
        parent = None
        curr = node

        # data에 해당하는 노드 찾기, parent 찾기
        while curr and curr.data != data:
            parent = curr

            if curr.data > data:
                curr = curr.left
            else:
                curr = curr.right

        # data를 못 찾은 경우
        if curr is None:
            return node
       
        # 자식 노드가 없는 노드의 삭제ㅓ
        if curr.left is None and curr.right is None:
            if curr != node:
                if parent.left == curr:
                    parent.left = None
                else:
                    parent.right = None
            else:
                node = None

        # 오른쪽과 왼쪽 모두 자식이 있는 경우
        elif curr.left and curr.right:
        # 지우려는 노드의 오른쪽 하위 트리에서 가장 작은 노드 찾기
            min_node = self.find_min_node(curr.right)

            min_data = min_node.data

            # 오른쪽 하위 트리에서 가장 작은 노드는 항상 잎새 노드이므로 
            # 바로 삭제
            self._delete_data(node, min_data)
            curr.data = min_data

            # 오른쪽 혹은 왼쪽 노드 하나만 있는 경우
        else:
            if curr.left:
                child = curr.left
            else:
                child = curr.right

            if curr != node:
                if curr == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                node = child

        return node
    # 잎새 노드를 지우는 경우 -> 부모 노드의 오른쪽/왼쪽 고리 끊기
    # 하나의 자식만 갖는 노드 -> 단일 자식을 지워지는 노드 부모와 연결하고 노드 삭제
    # 자식이 2개인 경우 -> 지우려는 노드의 '오른쪽' 하위 트리의 가장 작은 값으로 자신을 대체하면 전체 트리의 속성을 유지하면서 노드 삭제 가능함

    def inorder_traverse(self):
        result = []
        self._inorder_rec(self._root, result)
        return result

    def _inorder_rec(self, node, result):
        if not node:
            return
        self._inorder_rec(node.left, result)
        result.append(node.data)
        self._inorder_rec(node.right, result)
    
    def inorder_iter(self):
        result = []
        stack = []

        node = self._root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                result.append(node)
                node = node.right
        return result
if __name__ == "__main__":
    node = Node(11)
    print(node)
    bst = BinarySearchTree()
    arr = [15, 26, 30, 50]
    bst.insert(20, 'recursion')
    bst.insert(21, 'recursion')
    bst.insert(15, 'recursion')
    rr = bst.inorder_traverse()
    print(rr)
    for num in arr:
        bst.insert(num, method='iterative')
    result = bst.inorder_traverse()
    print(result)
    print("protected", bst._root)
    # print("private", bst.__test_root)
    bst.delete(15)
    result = bst.inorder_traverse()
    print(result)
