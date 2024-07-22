from collections import deque
# Definition for a binary tree node.
class treenode:
     def __init__(self, val=0, left=none, right=none):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # root is Null
        if not root:
            return False
        
        # Left BFS for left tree
        left_tree = root.left
        right_tree = root.right
        left_tree_array, right_tree_array = [], []
        left_queue = deque([left_tree.val])
        right_queue = deque([right_tree.val])

        while left_queue:
            next_left = left_queue.popleft()
            left_tree_array.append(next_left.val)
            if next_left.left:
                left_tree_array.append(next_left.left.val)
                left_queue.append(next_left.left)
            if next_left.right:
                left_tree_array.append(next_left.right.val)
                left_queue.append(next_left.right)

        
        while right_queue:
            next_right = right_queue.pop()
            right_tree_array.append(right_queue.val)
            right_queue.append(next_right)

        if left_tree_array == right_tree_array:
            return False

if __name__ == "__main__":
    sol = Solution()
    input = [1,2,2,3,4,4,3]
    root = Treenode(1)
    for node in input:


    print(sol.isSymmetric(root))
