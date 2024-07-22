def solution(l, r):
    answer = []
    for num in range(l, r+1):
        str_num = str(num)
        for char in str_num:
            #if char != "0" or char != "5":
            #    break
            #if (char != "0") or (char != "5"):
            #    print(num)
            #    break
            if not (char == "0" or char == "5"):
                break # 첫번째 for loop을 넘기고 싶음
        else:
            answer.append(num)
    if not answer:
        answer = [-1]
    return answer

if __name__ == "__main__":
    print(solution(5,50))
