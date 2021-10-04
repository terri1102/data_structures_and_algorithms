- 레퍼러로 어떤 웹페이지 거쳐왔는지 판별 : 
보통 호스트 단위로 집계

postgres의 경우
```sql
select 
stamp --referer의 호스트 이름 부분 추출
,substring(referrer from 'https?://([^/]*)') as referrer_host
from access_log;
```
