## 문제 933. Number of Recent Calls

## 출처
https://leetcode.com/problems/number-of-recent-calls/

## 풀이
```python
type RecentCounter struct {
    counter []int
}


func Constructor() RecentCounter {
    // queue
    counter := RecentCounter()
    return counter
}


func (this *RecentCounter) Ping(t int) int {
    counter1 := this.counter
    if t <= 3000 {
        counter1 = append(counter1, t)
        return len(counter1)
    } else {
        //pingRange := 3000-t, t
        for i := range counter1 {
            first := counter1[0]
            if first < 3000-t {
                counter1 = counter1[1:]
            }
        } 
        return len(counter1) 
    }
}


/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */
```
