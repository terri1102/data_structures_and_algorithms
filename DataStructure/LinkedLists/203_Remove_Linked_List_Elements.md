## 문제 203. Remove Linked List Elements

## 출처
https://leetcode.com/problems/remove-linked-list-elements/
## 풀이
혼자 풀었을 때도 더미 노드 추가하는 거랑 코드 거의 비슷했지만
while문에 조건 거는 거...는 비슷한 (코드 상 다르지만 결과는 같은...)
current_node.next = current_node.next.next 이 부분을 나는 dummy_head.next = dummy_head.next.next로 했었는데 여기서 자꾸 nonetype에 next없다고 에러 났었음

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                
        return dummy_head.next
```
