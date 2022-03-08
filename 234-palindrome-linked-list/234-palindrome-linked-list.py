# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp_list = []
        node = head
        while node:
            tmp_list.append(node.val)
            node = node.next
        reversed_list = tmp_list[::-1]
        if tmp_list == reversed_list:
            return True
        else:
            return False
            
        