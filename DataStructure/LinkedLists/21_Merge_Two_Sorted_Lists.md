## 문제 21. Merge Two Sorted Lists

## 출처
https://leetcode.com/problems/merge-two-sorted-lists/

## 풀이

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None and list2 is None:
            return None
        
        if list1 is not None and list2 is None:
             return list1
        elif list2 is not None and list1 is None:
            return list2
        
        merged_list = ListNode()
        curr = merged_list
        
        while list1 and list2: 
            if list1.val == list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
                
                curr.next = list2
                list2 = list2.next
                curr = curr.next
                
            elif list1.val > list2.val:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
            else:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
        
        
        #여기 예외처리...list1은 None이 되었는데 list2는 있는 경우와 그 반대
        if list1 is not None and list2 is None:
            while list1:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
        elif list2 is not None and list1 is None:
            while list2:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
            
        merged_list = merged_list.next
        return merged_list

```
