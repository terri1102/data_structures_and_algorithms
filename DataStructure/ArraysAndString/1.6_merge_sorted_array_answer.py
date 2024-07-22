from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # start from the end of nums1 and nums2
        p1, p2, k = m - 1, n - 2, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[k] = nums2[p2]
                p2 -= 1
            else:
                nums1[k] = nums1[p1]
                p1 -= 1
            k -= 1
        sample_list = [1,2,3,4,5]
        print(hex(id(sample_list)))
        # sample_list[:] = sorted(sample_list, reverse=True)
        sorted(sample_list, reverse=True)
        print(hex(id(sample_list)))
        sample_list.sort()
        print(hex(id(sample_list)))
        # If there are remaininig elements in nums2, copy them
        while p2 >= 0:
            nums1[k] = nums2[p2]
            p2 -= 1
            k -= 1


if __name__ == "__main__":
    case1_n1, case1_n2 = [1, 2, 3, 0, 0, 0], [2, 5, 6]
    s = Solution()
    s.merge(case1_n1, 3, case1_n2, 3)
    print(case1_n1)

