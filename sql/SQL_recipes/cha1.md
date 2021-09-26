코드를 레이블로 변경하는 쿼리
```sql
SELECT 
  user_id,
  CASE
    WHEN register_device = 1 THEN '데스크톱'
    --디폴트 값을 지정할 경우 ELSE 구문 사용
    ELSE '전자기기'
    END AS device_name
FROM users
```
