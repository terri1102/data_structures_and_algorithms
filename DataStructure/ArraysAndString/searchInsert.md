https://leetcode.com/problems/search-insert-position

"정렬된" 배열에서 목표값 찾는 것 -> 정렬되었기에 이진탐색 가능

Edge case로 빈 배열 고려하기

살제로 배열에 값을 넣어 정렬된 상태로 만드는 것이 아니라 target 값이 있는 위치 찾는 것

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1 
        while low <= high:
            mid = low+(high-low)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid -1
            else:
                low = mid +1
        return low

```
