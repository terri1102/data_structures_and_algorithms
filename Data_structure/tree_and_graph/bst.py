# Binary Search Tree 구현
import math

def solution(array, target):
    n = len(array)
    search_num = math.ceil(math.log2(n))
    # mid = n // 2
    low, high = 0, len(array)
    # !!!!!!!!!!!!! mid 업데이트시 n을 자꾸 쓰는 게 아니라 low와 high를 트래킹해야 함
    for _ in range(search_num):
        mid = (low+high)//2
        temp = array[mid]
        if temp == target:
            return mid
        elif temp < target:
            low = mid + 1
            #mid = (mid+n) // 2
        else:
            high = mid - 1
        #mid = mid // 2
    return False

if __name__ == "__main__":
    input = [1,2,3,5,6,7,8]
    target = 6
    result = solution(input, target)
    # assertTrue(result == input.index(target), f"{result}{input.index(target)}")
    
    print(result)
