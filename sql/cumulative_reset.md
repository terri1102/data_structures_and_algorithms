![image](https://user-images.githubusercontent.com/73813367/127149730-0a4034ae-1039-4099-80eb-16df13547b4e.png)

[sqlite db]

1. created_at(text)을 Date으로 불러옴(원래 문제에선 Datetime이었지만...sqlite db 만드는 과정에서 실수함) -> 실제 table이 바뀌는 건 아님
```sql
SELECT date(created_at) 
FROM test
```
2. window function으로 cumulative count reset

