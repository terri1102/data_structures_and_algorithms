## 문제 832. Flipping an Image


## 출처
https://leetcode.com/problems/flipping-an-image/


## 내 풀이

처음엔 아무 생각 없이
```
for row in image:
  row = row[::-1]
  for e in row:
    e = e^1
```
이런식으로 했더니 image의 값이 바뀌지 않았다. 당연히도...

enumerate을 쓰는 게 괜찮은지는 모르겠지만 일단 in place 방식으로 풀었다.

하지만 문제 카테고리가 two pointers니까 다른 정석적인 풀이가 있을듯

```python
class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        # horizontally 가로로 반전
        # invert 0과 1 반전
        
        for i, row in enumerate(image):
            image[i] = image[i][::-1]
            for idx, e in enumerate(row):
                image[i][idx] = image[i][idx] ^ 1      
        
        return image

```

## 문제에서 의도한 것 같은 풀이
i는 0부터 시작 j는 리스트의 끝부터 시작하는 투 포인터
```python
def flipAndInvertImage(self, A):
	for row in A:
		i, j = 0, len(row) - 1
		while i <= j:
			if row[i] == row[j]:
				row[i], row[j] = row[i]^1, row[j]^1
			i += 1
			j -= 1
	return A

```

## 다른 풀이
```python
  def flipAndInvertImage(self, A):
        return [[1 ^ i for i in reversed(row)] for row in A]
```
파이썬스럽게 list comprehension으로 한 줄로 풀었군
