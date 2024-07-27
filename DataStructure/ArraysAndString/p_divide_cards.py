def solution(arrayA, arrayB):
    answer = 0
    # Case1
    min_a = min(arrayA)
    
    for i in range(2, min_a + 1):
        for num in arrayA:
            if i == 14:
                breakpoint()
            if num % i != 0:
                continue
            break
        if (num % i == 0) and (i >= answer):
            answer = i
                
    for num in arrayB:
        if (answer != 0) and (num % answer == 0):
            answer = 0
    
    if answer != 0:
        return answer
    
    # Case2
    min_b = min(arrayB)
    
    for i in range(2, min_b + 1):
        for num in arrayB:
            if num % i != 0:
                continue
            break
        
        if (num % i == 0) and (i >= answer):
            answer = i
    
    for num in arrayA:
        if  (answer != 0) and (num % answer == 0):
            answer = 0
    return answer

if __name__ == "__main__":
    case1_a, case1_b = 	[14, 35, 119], [18, 30, 102]
    print(solution(case1_a, case1_b))
