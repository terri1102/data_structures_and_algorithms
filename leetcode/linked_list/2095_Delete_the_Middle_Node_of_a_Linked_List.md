## 문제 2095. Delete the Middle Node of a Linked List

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

## 출처
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

## Constraint
1. 1 <= Node.val <= 105
2. 중간 노드 2개일 때는 두번째 중간값 리턴
3. Linked List에 노드 하나이면 이를 제거하고 None 리턴

## 전략
1. Slow and fast pointer로 중간 노드 찾음
2. 중간 노드 앞 노드의 next를 중간 노드의 다음 노드 가리키게 함
3. 
O(N)

```python
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        # Edge case
        if not fast.next: # Linked List가 [1]일 때 빈 리스트 리턴
            head = None
            return head
        
        # 1. 중간 노드 찾기
        while fast and fast.next:
            prev = slow #slow 보다 한 칸 느림
            slow = slow.next
            fast = fast.next.next
            
        mid_next = slow.next
        
        # 2. prev의 next가 mid_next 가리키게 함
        prev.next = mid_next
        
        return head

```
