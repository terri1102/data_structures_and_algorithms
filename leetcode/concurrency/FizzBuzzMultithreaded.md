```python
from threading import Lock
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.locks = (Lock(), Lock(), Lock(), Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()
        self.locks[2].acquire()
      
    

    #0
    # divisible by 3
    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(self.n // 3 - self.n // 15):
            self.locks[0].acquire()
            printFizz()
            self.locks[3].release()
 
                 
    	
    # 1
    # divisible by 5 
    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(self.n // 5 - self.n // 15):
            self.locks[1].acquire()
            printBuzz()
            self.locks[3].release()
       
    	
    # 2
    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(self.n // 15):
            self.locks[2].acquire()
            printFizzBuzz()
            self.locks[3].release()

    # 3
    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n+1):
            self.locks[3].acquire()
            if i % 15 == 0:
                self.locks[2].release()
            elif i % 3 == 0:
                self.locks[0].release()
            elif i % 5 == 0:
                self.locks[1].release()
       
            else:
                printNumber(i)
                self.locks[3].release() 
```
