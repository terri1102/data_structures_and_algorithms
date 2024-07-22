from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1, ptr2 = 0, 0
        while ptr2 < n:
            if (ptr1 < m) and (nums1[ptr1] >= nums2[ptr2]):
                curr_left = nums1[ptr1:m]
                nums1[ptr1] = nums2[ptr2]
                nums1[ptr1+1:] = curr_left
                ptr2 += 1
            elif nums1[ptr1] < nums2[ptr2]:
                if not nums1[ptr1] == 0:
                    ptr1 += 1
                elif (nums1[ptr1] == 0):
                    curr_left = nums1[ptr1:m]
                    nums1[ptr1] = nums2[ptr2]
                    nums1[ptr1+1:] = curr_left
                    # nums1.insert(ptr1, nums2[ptr2])
                    ptr1 += 1
                    ptr2 += 1
    
        print(nums1)
if __name__ == "__main__":
    case1_n1, case1_n2 = [1,2,3,0,0,0], [2,3,6]
    s = Solution()
    print(s.merge(case1_n1, 3, case1_n2, 3))
