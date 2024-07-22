## 문제 206. Reverse Linked List

## 출처
https://leetcode.com/problems/reverse-linked-list/

## Contraint

## 풀이
curr, nextt, prev 3개의 포인터로 푸는 문제

1. 먼저 prev, curr를 None과 head로 initialize
2. nextt 포인터를 curr.next로 선언 (바로 다음에서 curr 노드의 next 방향이 바뀌기 떄문에 제일 먼저 해야함)
3. curr.next = prev (curr.next를 앞(NULL)을 가리키게 함)
4. prev = curr (prev 포인터를 curr 위치로 옮김)
5. curr = nextt (curr 포인터를 nextt 위치로 옮김)

순서 중요함!!

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        
        while curr:
            nextt = curr.next # 아래에서 바로 Linked List의 방향 바뀌니까 nextt 제일 먼저 옮겨야 함
            curr.next = prev
            prev = curr # prev를 curr 위치로 옮기고
            curr = nextt # curr를 nextt 위치로 옮김
        
        return prev #curr이 아니라 prev임
            
            
        
```
