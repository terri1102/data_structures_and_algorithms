
## 문제 

## 출처
https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/

## 풀이

뭔가 넌센스스러운 풀이였다...
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```

아래는 내가 삽질한 거

head 노드를 모르니까 삭제할 노드 앞 노드에 도달할 수 없음(prev 못 구함)

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        #head 안 됨
        # 삭제할 노드가 주어짐
        # 삭제할 노드는 TAIL 노드 아님 -> 삭제할 노드의 next는 None 아님
        
        # 1. 삭제할 노드의 prev 찾기
        # 2. 삭제할 노드의 prev의 next를 삭제할 노드의 next로 연결
        
        
        # 삭제할 노드의 next 노드 미리 찾아 놓기
        next_node = node.next
        
        
        # reverse
        prev, curr = None, node
           
        # while curr:
        while curr:
            nextt = curr.next # 아래에서 바로 Linked List의 방향 바뀌니까 nextt 제일 먼저 옮겨야 함
            curr.next = prev
            prev = curr # prev를 curr 위치로 옮기고
            curr = nextt # curr를 nextt 위치로 옮김
        print(prev, curr)
        
            
        #print(nextt) 9 #맨 마지막 노드
        #print(prev) # 1
 
   
        prev.next = next_node
  ```
