## Problem
연결리스트에서 cycle이 발견되면 true 리턴, 없다면 false 리턴

https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212

## Constraints
- The number of the nodes in the list is in the range [0, 104].
- -105 <= Node.val <= 105
- pos is -1 or a valid index in the linked-list.


## Edge case
- 빈 head가 주어진 경우 -> return False
- head가 노드 하나인 경우 -> return False


## Strategy
투 포인터

투 포인터는 보통
1. 포인터 하나는 앞에서, 다른 하나는 뒤에서 출발해서 탐색
2. 두 포인터가 다른 스피드로 이동하며 탐색
하는 방식으로 사용된다.
Singly Linked List에서는 포인터가 뒤에서 출발할 수 없기 때문에(Doubly Linked List여야 가능) 2번째 전략으로 탐색한다.

ptr1과 ptr2가 같아지면 순회가 끝나게 while문에 조건 걸기
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        
        ptr1 = head
        ptr2 = head.next
        
        while ptr1 != ptr2:
            if ptr2.is None or ptr2.next is None:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            
        return True

```

처음에 잘못 푼거...
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not (head.next) or (head):
            return False
        
        ptr1 = head
        ptr2 = head.next
        
        while (ptr1.next is not None) & (ptr2.next.next is not None):
            if ptr1.val == ptr2.val:
                return True
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            
        return False

```

ListNode에 size attribute이 있었으면 순회가 쉬워질 거 같음.

