https://leetcode.com/problems/combine-two-tables/submissions/

LEFT OUTER JOIN : LEFT OUTER JOIN 뒤에 나오는 테이블의 값이 없을 때 join하면 NULL값 나옴

```sql
--Write your MySQL query statement below
SELECT p.FirstName, p.LastName, a.City, a.State 
FROM Person p
LEFT OUTER JOIN Address a
ON p.PersonId = a.PersonId
```
