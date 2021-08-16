https://leetcode.com/problems/second-highest-salary/

두번째로 높은 임금
아래 코드는 5개 패스했음.
테스트케이스로 레코드가 하나인 경우도 있어서 거기서 걸림. [null] 나와야 함
```mysql
# Write your MySQL query statement below
SELECT Salary as SecondHighestSalary FROM Employee
Group By Salary
ORDER BY Salary DESC
Limit 1,1;
```
맞는 코드
```mysql
SELECT MAX(SALARY) AS SECONDHIGHESTSALARY FROM EMPLOYEE WHERE SALARY < (SELECT MAX(SALARY) FROM EMPLOYEE)
```
