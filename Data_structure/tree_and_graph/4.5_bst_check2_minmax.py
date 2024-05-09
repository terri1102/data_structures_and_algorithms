# 이진 탐색 트리의 정의
# -> 각 노드에서 left.data <= current.data < right.data를 만족하는 것
# 오른쪽 부등식에는 등호 안 붙는 것 주의

# 트리 탐색하며, 왼쪽으로 분기하면 max를 갱신하고,
# 오른 쪽으로 분기하면 min을 갱신함
from typing import Optional, Self


class Node:
    def __init__(
        self, data: int = 0, left: Optional[Self] = None, right: Optional[Self] = None
    ) -> None:
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self, root: Optional[Node] = None):
        self.root = root

    def is_bst(self):
        return self._check_bst(self.root, None, None)

    def _check_bst(
        self, node: Optional[Node], min: Optional[int], max: Optional[int]
    ) -> bool:
        if node is None:
            return True

        if (min is not None and node.data <= min) or (
            max is not None and node.data > max
        ):
            return False
        if not self._check_bst(node.left, min, node.data) or not self._check_bst(
            node.right, node.data, max
        ):
            return False
        return True


if __name__ == "__main__":
    node3 = Node(3)
    node7 = Node(7)
    node5 = Node(5, node3, node7)

    tree = BST(node5)
    print("Is the tree a BST?", tree.is_bst())
