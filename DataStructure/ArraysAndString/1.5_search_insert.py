from typing import List
def searchInsert(nums: List[int], target: int) -> int:
    if not nums:
        return 0
    
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums) # 맨 마지막에 삽입시

def binarysearchInsert(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1 
    while low <= high:
        mid = (low+high)//2 
        if nums[mid] > target:
            high = mid - 1 
        elif nums[mid] < target:
            low = mid + 1
        else:
            return mid
    return low
if __name__ == "__main__":
    nums1, target1 = [1,2,4,5,8,10,11], 10
    nums2, target2 = [], 2
    nums3, target3 = [1,3,6,7,11,13], 8
    nums4, target4 = [1,4,5], 6
    print(binarysearchInsert(nums1, target1))
    print(binarysearchInsert(nums2, target2))
    print(binarysearchInsert(nums3, target3))
    print(binarysearchInsert(nums4, target4))
