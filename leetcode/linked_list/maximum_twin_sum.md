## 문제
![image](https://user-images.githubusercontent.com/73813367/157447124-a60a46fc-90c2-435f-8178-5cb13eff0128.png)


## 출처
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

## 좋은 풀이
Runtime: 944 ms, faster than 93.16% of Python3 online submissions for Maximum Twin Sum of a Linked List.
Memory Usage: 45.1 MB, less than 89.45% of Python3 online submissions for Maximum Twin Sum of a Linked List.

투 포인터 전략 중에 fast pointer, slow pointer를 이용해서 풀었다

투 포인터 전략
1. forward pointer는 리스트 처음부터 순회, backward pointer는 뒤에서부터 순회
2. fast pointer는 두 칸씩(한 칸보다 크게) 전진, slow pointer는 한 칸씩 전진

나는 링크드 리스트의 전체 사이즈를 모르니까 새로운 배열 하나를 아예 하나 만들어서 순회했는데, 이 풀이는 linked list의 중간 값을 구한 다음에 이 뒷 부분만 뒤집는다 
(링크드 리스트 풀 때마다 Node 클래스에 size랑 prev attribute 넣고 싶어짐... )

1. linked list의 중간(slow)을 구한다. O(n/2)
2. 위에서 구한 slow를 이용해서 reversed linked list를 구한다. O(n/2)
3. 위에서 구한 prev가 head인 reversed linked list와 원래 linked list의 head를 더해서 가장 큰 값을 구한다. O(n/2)

```python
def pairSum(self, head: Optional[ListNode]) -> int:
	slow, fast = head, head
	maxVal = 0

	# Get middle of linked list
	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next

	# Reverse second part of linked list
	curr, prev = slow, None

	while curr:       
		curr.next, prev, curr = prev, curr, curr.next   

	# Get max sum of pairs
	while prev:
		maxVal = max(maxVal, head.val + prev.val)
		prev = prev.next
		head = head.next

	return maxVal
```


## 내 풀이

Runtime: 1708 ms, faster than 12.87% of Python3 online submissions for Maximum Twin Sum of a Linked List.
Memory Usage: 54.7 MB, less than 62.05% of Python3 online submissions for Maximum Twin Sum of a Linked List.

결과에서 볼 수 있듯이 엄청 느린 풀이..
Reversed_list를 구하기 위해 모든 node를 순회하고 O(n), 이렇게 만든 배열을 순회 O(n/2)하기 때문에 느림.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        reversed_list = []
        node = head
        while node:
            reversed_list.append(node.val)
            node = node.next
        
        forward = 0
        backward = len(reversed_list) - 1
        largest = -1
        for i in range(len(reversed_list)//2):
            tmp_sum = reversed_list[forward] + reversed_list[backward]
            if tmp_sum > largest:
                largest = tmp_sum
            forward += 1
            backward -=1
        return largest

```
