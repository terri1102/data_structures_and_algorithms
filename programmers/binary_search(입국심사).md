## 문제 설명
n명이 입국심사를 위해 줄을 서서 기다리고 있습니다. 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다.

처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다. 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다. 하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.

모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.

입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때, 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.

## 제한사항
입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.

각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.

심사관은 1명 이상 100,000명 이하입니다.

## 입출력 예
|n|	times	|return|
|6|	[7, 10]	|28|

## 문제 풀이
블로그에서 본대로 범위 설정과 기준을 정하는 게 중요한 것 같다.

범위: 1 ~ 심사를 하는 데 걸리는 가장 비효율적인 시간

기준: mid 동안 심사한 사람의 수가 n 보다 크면 right를 mid -1 로 하고,
심사한 사람의 수가 n보다 작으면 left를 늘린다.

근데 드는 생각은...이 문제만 보고 이분 탐색 문제인지 알아내는 것이 더 어려운 거 같다...ㅎ

```python
def solution(n, times):
    answer = 0
    
    #right - most inefficient case : n * max(times)
    left, right = 1, max(times) * n
    
    while left <= right:
        mid = (left + right) //2 
        people = 0
        for time in times:
            #people : all people who has done immigration check
            people += mid // time
            # if we can check n people in mid time, break
            if people >= n:
                break
        
        # if people >= n
        if people >= n:
            answer = mid
            right = mid -1
        # if people < n
        elif people < n:
            left = mid + 1
    return answer 
if __name__ == "__main__":
    print(solution(6, [7,10]))

```


풀이 출처: https://sohee-dev.tistory.com/123
