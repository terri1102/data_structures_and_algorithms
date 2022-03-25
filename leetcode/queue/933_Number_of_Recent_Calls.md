## 문제 933. Number of Recent Calls

## 출처
https://leetcode.com/problems/number-of-recent-calls/

## 풀이
```python
type RecentCounter struct {
    counter []int
}


func Constructor() RecentCounter {
    return RecentCounter{[]int{}}
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

```
type RecentCounter struct {
    t []int
}


func Constructor() RecentCounter {
    return RecentCounter{ []int{} }
}


func (this *RecentCounter) Ping(t int) int {
    this.t = append(this.t, t)
    for len(this.t) > 0 && this.t[0] + 3000 < t { this.t = this.t[1:] }
    return len(this.t)
}


```
