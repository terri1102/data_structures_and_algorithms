## 문제
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

## 출처
https://leetcode.com/problems/middle-of-the-linked-list/submissions/

## 풀이
- CONSTRAINT
 1. 노드 값 범위 1~100
 2. 중간값이 2개 일 때 두 번째 중간 값 리턴

- 전략
 - fast pointer, slow pointer 전략
 - O(n)

어제 푼 문제랑 비슷했다.(maximum twin sum)
이 문제의 투 포인터 전략을 이용해서 maximum twin sum 문제를 풀 수 있음
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        
        while fast.next and fast.next.next: 
            fast = fast.next.next
            slow = slow.next
        if fast.next != None: #linked list의 길이가 짝수인 경우
            slow = slow.next
        return slow
 ```
