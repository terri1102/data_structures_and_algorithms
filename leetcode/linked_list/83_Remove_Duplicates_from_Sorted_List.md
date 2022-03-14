## 문제
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

## 출처
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

## 풀이
정렬된 링크드 리스트이기 때문에 prev노드랑 현재 노드랑 비교하면서 한칸 씩 전진하면 됨
- None일 경우 항상 생각하기
- 대충 되겠거니 하지 말고 헷갈리면 그려보기

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # constraints
        # sorted list임
        
        if head is None:
            return None
        
        prev, node = head, head.next
        
        while node:
            if prev.val == node.val:
                prev.next = prev.next.next
                node = node.next
            else:
                prev = prev.next
                node = node.next
        
        return head

```
