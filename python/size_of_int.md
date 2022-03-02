
```python
import sys
print(2**0)
print(sys.getsizeof(0))
print(sys.getsizeof(3)) # 28
print(2**30)
print(sys.getsizeof(2**30)) # 32
print(sys.getsizeof(2**60)) # 36
print(sys.getsizeof(1.5)) # 24

# 0<=n < 2** 0 # 24 bytes # 0일 때
# 2**0 <= n < 2**30 # 28 bytes # 1~2^30-1
# 2** 30 <= n < 2** 60 # 32 bytes # 2^30 ~ 2^60 -1
#https://stackoverflow.com/questions/63483245/how-does-python-manage-size-of-integers-and-floats
# https://jakevdp.github.io/PythonDataScienceHandbook/02.01-understanding-data-types.html

# ob_refcnt, ob_type, ob_size, ob_digit[1] 을 가지는 STRUCT
```
