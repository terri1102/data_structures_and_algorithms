## 문제 1700. Number of Students Unable to Eat Lunch


## 출처
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/submissions/

```python
class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        while students and (sum(students) ^ sum(sandwiches) !=1):
            if students[0] == sandwiches[0]:
                students = students[1:]
                sandwiches = sandwiches[1:]
               
            else:
                tmp_sandw = sandwiches[0]
                tmp_stu = students[0]
                sandwiches = sandwiches[1:].append(tmp_sandw)
                students = students[1:].append(tmp_stu)
        
        if not students:
            return 0
        return len(students)
        
```
