## 문제 146. LRU Cache


## 출처
https://leetcode.com/problems/lru-cache/

## 풀이

```python
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = None #여기서 head는 노드 객체 아니고 key
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache.keys():
            self.head = key
            return self.cache[key]
        else:
            return -1
        
        
        # if self.cache[key]: # cache에 key없으면 에러남
        #     return self.cache[key]
        # return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
      
            
        # key 있으면 update
        
        if key in self.cache.keys():
            self.cache[key] = value
        
        # key 없으면
        else:   
            if self.size < self.capacity:
                self.cache[key] = value
                self.size += 1
                #self.tail = self.head
                self.head = key
                
            else:
                del self.cache[self.tail]
                self.tail = self.head
                self.cache[key] = value
                self.head = key
        
        if self.size == 1:
            self.tail = key
                
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```
