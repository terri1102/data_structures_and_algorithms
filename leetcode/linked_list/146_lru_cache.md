## 문제 146. LRU Cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

## 출처
https://leetcode.com/problems/lru-cache/

## 풀이
```python
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity):
        self.cache = {} #key to node
        self.capacity = capacity
        self.head = ListNode(0,0)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove_from_list(node)
            self.insert_into_head(node)
            return node.value
        else:
            return -1
    
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self.remove_from_list(node)
            self.insert_into_head(node)
            node.value = value
        else:
            if len(self.cache) >= self.capacity:
                self.remove_from_tail()
            node = ListNode(key, value)
            self.cache[key] = node
            self.insert_into_head(node)
    
    def remove_from_list(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def insert_into_head(self, node):
        head_next = self.head.next 
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node
        
    def remove_from_tail(self):
        if len(self.cache) == 0:
            return
        tail_node = self.tail.prev
        del self.cache[tail_node.key]
        self.remove_from_list(tail_node) 

```

tail을 업데이트하는 부분을 고쳐야 함
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
