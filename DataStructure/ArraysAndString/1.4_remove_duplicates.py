# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def deduplicate_before(array):
    if not array:
        return 0

    prev = array[0]
    to_delete = []

    for i in range(1, len(array)):
        if array[i] == prev:
            to_delete.append(i)
        
        prev = array[i]
    print(hex(id(array)))
    array = [array[i] for i in range(len(array)) if i not in to_delete]
    
    print(hex(id(array)))

    return len(array)

def deduplicate(array):
    if len(array) < 2:
        return len(array)
    prev = array[0]
    pointer = 1 
    while pointer < len(array):
        if array[pointer] == prev:
            array.pop(pointer)
        else:
            prev = array[pointer]
            pointer += 1
    print(array)

    return len(array)
if __name__ == "__main__":
    array1 = [1,2,2,3,3]
    array2 = [1,1,2,4,5]
    array3 = [1]
    print(deduplicate(array1))
    print(deduplicate(array2))
    print(deduplicate(array3))
