



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
