from typing import List
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    for i, nums1_item in enumerate(nums1):
        if nums1_item > nums2[0]:
            nums1[i] = nums2[0]
            nums2[0] = nums1_item

            for k, item in enumerate(nums2[1:], start=1):
                if nums1_item <= item:
                    nums2[k-1] = nums1_item
                    break
                nums2[k-1] = nums2[k]

