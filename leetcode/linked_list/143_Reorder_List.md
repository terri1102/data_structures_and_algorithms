## 문제
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …


## 출처
https://leetcode.com/problems/reorder-list/

## CONSTRAINT


## 풀이


```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        # 1. slow, fast pointer로 mid 구함
        slow = fast = head
        
        cnt = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            cnt += 1

        
        # 2. Reverse half end
        # 이 부분이 어려웠음
        curr, prev = slow, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next #found circle!!

        reversed_head = prev    
        
        # 3. Cut original linked list half 
        slow.next = None
        
        # 4. 순회하며 짝수일 때, 홀수 일 때 하나씩 연결
        for i in range(cnt):
            if i // 2:
                head.next = reversed_head
                head = head.next
            else:
                reversed_head.next = head
                reversed_head = reversed_head.next

        
```
