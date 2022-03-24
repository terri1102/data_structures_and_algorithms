## 문제 1614. Maximum Nesting Depth of the Parentheses

## 출처
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

## 풀이
'('가 나오면 count를 세고, ')'가 나오면 count를 빼면 된다.

## Go..
처음에 파이썬에서 쓰던대로.."("로 썼더니 rune과 untyped string을 비교하지 말라는 에러가 떴다.

그래서 '('로 rune 타입으로 바꿔서 비교함


```go
func maxDepth(s string) int {
    var maxNum int = 0
    var currNum int = 0
    
    for _, c := range s { 
       
        if  c == '(' {
            currNum += 1
            if currNum > maxNum {
                maxNum = currNum
            }
        } else if c == ')' {
            currNum -= 1
            }
        }
    return maxNum
    }
```
