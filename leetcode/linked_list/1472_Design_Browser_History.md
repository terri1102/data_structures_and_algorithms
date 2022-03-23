## 문제 1472. Design Browser History

## 출처
https://leetcode.com/problems/design-browser-history/

## 내 풀이
1. 일단 Node class 만들어서 next와 prev 포인터를 사용할 수 있게 함
2. 이전에 방문한 사이트와 이후에 방문한 사이트 모두 기억해야 하기 때문에 doubly linked list로 만들었다.
3. None값 에러처리
4. Head와 Tail을 이용한 에러처리

## 개선점
1. 에러 처리: None값이 입력으로 들어오는 경우과 함수 안에서 None이 되는 경우를 잘 생각해보자.
2. prev : doubly linked list여서 prev도 써야 하는데 자꾸 함수 구현에서 까먹었음
3. head와 tail 모두 사용하는 게 맞을까?

제출 결과가 엄청 좋지는 않다. 보니까 스택으로 푸는 방법 vs. 이중 연결 리스트 구도 던데

Runtime: 372 ms, faster than 36.16% of Python online submissions for Design Browser History.

Memory Usage: 16.7 MB, less than 9.59% of Python online submissions for Design Browser History.

```python
class UrlNode(object):
    def __init__(self, url):
        self.value = url
        self.next = None
        self.prev = None

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.head = UrlNode(homepage)
        self.tail = self.head
        self.curr = self.head
        #self.visited_urls = [homepage] # 이런 거 이상하게 맨날 만들고 싶은데...메모리나 더 차지 하니 생략하자
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        if self.curr is None:
            return
        tmp = self.curr
        self.curr.next = UrlNode(url)
        self.curr = self.curr.next
        self.curr.prev = tmp
        self.tail = self.curr
     
        
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and self.curr is not None and self.curr is not self.head:
            tmp = self.curr
            self.curr = self.curr.prev
            self.curr.next = tmp
            steps -= 1
        if self.curr is None:
            return 
        
        #if self.curr == self.head: #while문에서 처리되기 때문에빠져도 되는 부분
        #    return self.curr.value
        return self.curr.value
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.curr is None:
            return
        if self.curr.next is None:
            return self.curr.value
        while (steps > 0) and (self.curr is not None) and (self.curr is not self.tail):
            tmp = self.curr
            self.curr = self.curr.next
            #if self.curr is not None: # 이거 없이 while문 밖으로 나가야 하는 거 아님?? 위의 while문에서 tail로 처리해서 이제 self.curr이 None인 거 검사 안 해도 
            #    self.curr.prev = tmp
            steps -= 1
       
        if self.curr is None:
            return
 
        return self.curr.value
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


```
