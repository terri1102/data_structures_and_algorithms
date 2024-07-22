from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        return nums
    def rotate2(self, nums: List[int], k: int) -> None:
        temp = [0 for _ in range(len(nums))]
        n = len(nums)
        temp[k:] = nums[:k]        
        temp[:k] = nums[k:]
        nums[:] = temp[:]
        return nums

if __name__ == "__main__":
    s = Solution()
    case1_nums = [1,2,3,4]
    case1_k = 1
    case2_nums = [1,2]
    case2_k = 3
    print(s.rotate(case1_nums, case1_k))
    print(s.rotate(case2_nums, case2_k))
    print(s.rotate2(case1_nums, case1_k))
    print(s.rotate2(case2_nums, case2_k))
