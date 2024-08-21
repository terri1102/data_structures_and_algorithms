# 문제: 112. Path Sum
https://leetcode.com/problems/path-sum/

## 아이디어
- 트리 아래로 가면서 재귀로 new_sum을 업데이트 하다가 노드 값과 같으면 True 리턴
- 왼쪽과 오른쪽을 순회하며는 것을 `or`로 연결해서 하나라도 True이면 True가 될 수 있게 함

## 풀이
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum):
    if not root:
        return False
    
    # 리프 노드에 도달했을 때, 경로의 합이 targetSum과 같은지 확인
    if not root.left and not root.right:
        return root.val == targetSum
    
    # 왼쪽과 오른쪽 서브트리에서 경로의 합을 확인
    new_sum = targetSum - root.val
    return hasPathSum(root.left, new_sum) or hasPathSum(root.right, new_sum)

# 예제 트리
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

targetSum = 22
print(hasPathSum(root, targetSum))  # 출력: True

```
## 배운 점
- 재귀 문제에서 `return func(1) or func(2)` 이런 식으로 쓰는 방식
    - func(1)을 호출하고 func(1)이 종료되면 func(2)를 호출함
    - 하나라도 True면 마지막 결과가 True가 됨
    - 단락 평가(short-circuit evaluation)
: func(1)이 Truthy면 func(2)는 실행되지 않음