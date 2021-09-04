
주사위를 던져서 같은 눈이 나온 개수를 세는 문제
```python
n = int(input())

dice_dict = {}
result_list = []
for _ in range(n):
  dice_list = list(map(int, input().split()))
  for num in dice_list:
    dice_dict[num] = dice_list.count(num)   ##이 부분이 중요
    for k, v in dice_dict.items():
      if v == 3:
        result = 10000 + k * 1000
      elif v ==2:
        result = 1000 + k * 100
      else:
        result = 100 * sorted(dice_dict, reverse=True)[0]
      result_list.append(result)

result_list.sort(reverse=True)
print(result_list[0])

```
