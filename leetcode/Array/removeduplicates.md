## 문제 링크 https://leetcode.com/problems/remove-duplicates-from-sorted-array/

## 문제
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


## 풀이
중복된 값이 아닐 때 커서를 하나씩 옮겨주면 된다
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        curr = nums[0]
        cur_index = 1
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] != curr:
               curr = nums[i]
               nums[cur_index] = curr
               cnt += 1
               cur_index += 1
        
                
        return cnt + 1
```
