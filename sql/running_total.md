
https://codingsight.com/calculating-running-total-with-over-clause-and-partition-by-clause-in-sql-server/


StudentAge 칼럼의 누적 SUM, AVG를 구함
```sql
USE School
SELECT Id, StudentName, StudentGender, StudentAge,
SUM (StudentAge) OVER (ORDER BY Id) AS RunningAgeTotal,
AVG (StudentAge) OVER (ORDER BY Id) AS RunningAgeAverage
FROM Students

```
