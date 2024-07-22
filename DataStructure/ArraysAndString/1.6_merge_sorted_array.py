from typing import List
def mergeSortedArray(nums1: List[int], nums2: List[int]) -> List[int]:
    cnt1, cnt2 = 0, 0
    while cnt2 < len(nums2):
        if (cnt1 < len(nums1)) and (nums1[cnt1] >= nums2[cnt2]):
            nums1.insert(cnt1, nums2[cnt2])
            # print(nums1) 
            cnt2 += 1
        elif (cnt1 < len(nums1)) and (nums1[cnt1] < nums2[cnt2]):
            cnt1 += 1
        else: # nums2가 남아있는 경우
            nums1.insert(cnt1, nums2[cnt2])
            cnt2 += 1
            cnt1 += 1
    return nums1

if __name__ == "__main__":
    case1_n1, case1_n2 = [1,2,4,7,11,20,41], [5,6,13,42]
    case2_n1, case2_n2 = [5,6,9], [1,3,7]
    case3_n1, case3_n2 = [6,6,7,8], [6,9,10]
    case4_n1, case4_n2 = [1,2,3,0,0,0], [2,5,6]
    case5_n1, case5_n2 = [1], []

    print(mergeSortedArray(case1_n1, case1_n2))
    print(mergeSortedArray(case2_n1, case2_n2))
    print(mergeSortedArray(case3_n1, case3_n2))
    print(mergeSortedArray(case4_n1, case4_n2))
    print(mergeSortedArray(case5_n1, case5_n2))

