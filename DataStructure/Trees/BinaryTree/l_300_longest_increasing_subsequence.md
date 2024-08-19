# 문제: 300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/description/

숫자 배열이 주어지면 strict 오름차순으로 증가하는 부분 배열 중 가장 긴 배열의 길이 구하기


## 아이디어
- (인덱스, 값)으로 튜플 정렬한 다음에 풀려고 했으나 풀지 못했음
### 다이나믹 프로그래밍
- nums 길이로 dp 배열을 1로 초기화
- 1에서 nums 길이까지 i로 순회하면서(substring), 다시 i까지 j로 순회하며(substring 내 오름차순 검증)
- nums[i]가 nums[j]보다 크면 dp[i]에 dp[i]와 dp[j]+1 중 더 큰 값을 기록함.
- i = 1 substring [10] -> dp[1] = 1
- i = 2 substring [10,9] (오름차순 아님) -> dp[2] = 1
- 예를 들면 i=3이면 substring은 [10,9,2]이고 j=0, 1, 2이다.
    - nums[i]는 5 < nums[j]는 10 -> pass(오름차순 아님)
    - nums[i]는 5 < nums[j]는 9 -> pass 
    - nums[i]는 5 > nums[j]는 2 -> 오름차순
        - dp[3] = max(1, dp[2]+1) = 2
    - 여기서 dp[j]+1 인 이유는 nums[i] > nums[j]이면 오름차순인 배열 길이가 하나씩 길어지기 때문
- 이런 식으로 앞에서부터 하나씩 substring을 구한 후 그 substring 내에서 가장 긴 오름 차순인 substring의 길이를 max로 구한다.
    
### 이분 탐색
- lis 리스트: 이 리스트는 현재까지의 증가하는 부분 수열을 표시. 이 리스트는 실제 LIS는 아니지만 LIS의 길이를 추적하는 데 사용됨
- bisect_left 사용: bisect_left(lis, num) 함수는 lis 리스트에서 num이 들어갈 위치를 이분 탐색으로 찾아냄. 만약 num이 lis의 마지막 요소보다 크다면, 새로운 요소를 리스트 끝에 추가함. 그렇지 않으면, 해당 위치의 요소를 num으로 대체함
- lis 리스트 업데이트: 리스트의 길이는 항상 LIS의 길이와 일치함. 따라서, 최종적으로 lis 리스트의 길이를 반환.


## 풀이
### 다이나믹 프로그래밍
```python
class Solution
    def lengthOfLIS(nums):
        
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

# 예제 실행
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))  # 출력: 4

```

### 이분 탐색
1. lis 배열 초기화
2. nums 배열을 하나씩 순회하면서 정렬된 lis에 정렬을 유지하면서 num을 넣을 때의 위치를 구함.
3. 만약 pos가 lis 길이보다 작으면 pos 위치에 lis[pos] = num으로 업데이트
4. 아니라면 lis에 num을 append함


```python
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for num in nums:
            pos = bisect.bisect_left(lis, num)
            if pos < len(lis):
                lis[pos] = num
            else:
                lis.append(num)
        
        return len(lis)    

```
## 배운 점
- 문제를 풀지 못했는데 DP와 이분 탐색으로 푸는 법을 찾아 이해하려고 했음
- bisect.bisect_left(a,x): 정렬된 순서를 유지하도록 a에 x를 삽입할 위치를 찾음