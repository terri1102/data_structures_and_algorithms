class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class BST:
    def __init__(self, root=None):
        self.root = root
        self.tree = []

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current_node, key):
        if current_node is None:
            return False
        if key == current_node.key:
            return True
        elif key < current_node.key:
            return self._search(current_node.left, key)
        elif key > current_node.key:
            return self._search(current_node.right, key)

    def find_node(self, key):
        return self._find_node(self.root, key)

    def _find_node(self, current_node, key):
        if current_node is None or current_node.key == key:
            return current_node
        elif current_node.key < key:
            return self._find_node(current_node.right, key)
        else:
            return self._find_node(current_node.left, key)

    def delete(self, key):
        node_to_delete = self.find_node(key)
        if node_to_delete is None:
            return False

        # Case 1: Node to delete is a leaf node
        if node_to_delete.left is None and node_to_delete.right is None:
            self._delete_leaf(node_to_delete)
        # Case 2: Node to delete has a child node
        elif node_to_delete.left is None or node_to_delete.right is None:
            self._delete_node_with_one_child(node_to_delete)
        # Case 3: Node to delete has two children node
        else:
            self._delete_node_with_two_children(node_to_delete)

    def _delete_leaf(self, node):
        if node.parent is None:
            self.root = None
        elif node == node.parent.left:
            node.parent.left = None
        else:
            node.parent.right = None

    def _delete_node_with_one_child(self, node):
        if node.left is not None:
            child = node.left
        else:
            child = node.right
        if node.parent is None:
            self.root = child
        elif node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child
        child.parent = node.parent

    def _delete_node_with_two_children(self, node):
        # Find the in-order successor (smallest node in the right subtree)
        successor = self._leftmost(node.right)
        node.key = successor.key  # Copy the successor's key to the node
        # Delete the successor
        if successor.parent.left == successor:
            successor.parent.left = successor.right
        else:
            successor.parent.right = successor.right
        if successor.right is not None:
            successor.right.parent = successor.parent

    def in_order_successor(self, key):
        node = self.find_node(key)
        if node is None:
            return None
        # 1. If right subtree exists
        if node.right is not None:
            return self._leftmost(node.right)

        # 2. If no right subtree exists, look for the lowest ancestor
        while node.parent is not None and node == node.parent.right:
            node = node.parent
        return node.parent

    def _leftmost(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


if __name__ == "__main__":
    bst = BST()
    # bst.insert(50)
    # bst.insert(30)
    # bst.insert(70)
    # bst.insert(20)
    # bst.insert(40)
    # bst.insert(60)
    # bst.insert(80)
    # print(bst.search(40))
    values = [2, 3, 4, 5, 6, 7, 8]
    for value in values:
        bst.insert(value)
    successor_node = bst.in_order_successor(7)
    if successor_node:
        print(f"The inorder successor of 7 is {successor_node.key}")
    else:
        print("There is no inorder successor of 7")
