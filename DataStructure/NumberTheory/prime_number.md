## 소수의 개수 구하기
에라토스테네스의 체 이용
```python
def num_of_prime(n):
  cnt = 0
  net = [0] * (n+1)   
  for i in range(2, n):
    if net[i] = 0:
      cnt += 1
      for j in range(i, n+1, i):
        net[j] = 1
  return cnt

```

## 소수 판별 
```python
def isPrime(n):
  if n == 1:
    return False
  for i in range(2, n//2+1): #약수는 자신의 절반까지만 존재함
    if n % i == 0:
      return False
   else:
    return True
```
