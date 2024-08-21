# 문제: 436. Find right interval
https://leetcode.com/problems/find-right-interval/description/

## 아이디어
- interval의 시작은 unique하기 때문에 시작 기준으로 정렬
- 정렬 후 interval의 끝 기준으로 어디에 삽입해야 할지 위치를 찾음
- 찾은 위치의 interval의 원래 인덱스를 answer에 append함
- original_dict을 사용해서 {(interval 시작, interval 끝): [intervals 배열의 인덱스, right_interval의 intervals 인덱스]} 저장함

## 풀이
1. intervals에 요소가 하나인 경우 처리
2. original_dict에 intervals의 요소를 튜플로 바꾼 값을 키로, 인덱스를 값으로 저장함
3. intervals을 시작 원소 기준으로 정렬해 sorted_intervals 배열을 만듦
4. sorted_intervals의 시작값들을 starts 배열로 만듦
5. sorted intervals를 순회하며 끝 원소가 starts 배열의 어느 위치에 들어가야 하는지 bisect.bisect_left로 찾음
    5-1. 만약 맨 마지막 위치면 -1을 append
    
    5-2. 만약 맨 마지막 위치가 아니면 right_interval을 sorted_intervals[위치]로 구하고 original_dict에서 원래 배열의 인덱스를 구함. 그 후 original_dict의 키 값(리스트)에 인덱스를 값을 append함

6. intervals를 순회하면서 original_dict의 리스트의 두 번째 값을 append함
```python
import bisect
from collections import defaultdict
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:  
        if len(intervals) == 1:    
            if intervals[0][0] == intervals[0][1]:
                return [0]
            elif intervals[0][0] < intervals[0][1]:
                return [-1]
        
        original_dict = {(start, end):[i] for i, (start, end) in enumerate(intervals)}
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        answer = []
        starts = [start[0] for start in sorted_intervals]
        for i, sorted_interval in enumerate(sorted_intervals):
            if i == len(sorted_intervals) - 1:
                original_dict[tuple(sorted_interval)].append(-1)
            else:
                # pos: bisect_right로 하면 틀림! 길이 밖의 값 리턴함
                pos = bisect.bisect_left(starts, sorted_interval[1])
                
                if pos == len(sorted_intervals):
                    original_dict[tuple(sorted_interval)].append(-1)
                else:
                    right_interval =  sorted_intervals[pos]
                    right_interval_orig_idx = original_dict[tuple(right_interval)][0]

                    original_dict[tuple(sorted_interval)].append(right_interval_orig_idx)
                    
        for interval in intervals:
            right_interval_index = original_dict[tuple(interval)][1]
            answer.append(right_interval_index)
        
        return answer

        
```
## 배운 점
- bisect.bisect_left, bisect.bisect, bisect.bisect_right의 차이
 - bisect_left: 주어진 정렬된 리스트에서 x가 들어갈 수 있는 가장 왼쪽(앞쪽) 위치를 반환 -> 이 문제는 가능한 인덱스의 최소값 구하는 것이기에 적합함
 - bisect, bisect_right: 주어진 정렬된 리스트에서 x가 들어갈 수 있는 가장 오른쪽(뒤쪽) 위치를 반환