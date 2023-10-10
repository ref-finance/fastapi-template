# fastapi-template
Pthon 3.10 + 

## run script
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt

create_your app into ./apps file
add app name into settings.config file
```python
APPLICATIONS = [
    'test_app'
]
```


## Integrated functions
### log file output
./logs/app_main.log
./logs/app_main_debug.log
```
[INFO]:[core.init_app]: rid=bc04f010ce5f0611 start request path=/ (2023-10-10 18:25:07; init_app.py:44)
[INFO]:[core.init_app]: rid=bc04f010ce5f0611 completed_in=2.59ms status_code=404 (2023-10-10 18:25:07; init_app.py:51)
[INFO]:[core.init_app]: rid=64667dd521977971 start request path=/favicon.ico (2023-10-10 18:25:07; init_app.py:44)
[INFO]:[core.init_app]: rid=64667dd521977971 completed_in=0.44ms status_code=404 (2023-10-10 18:25:07; init_app.py:51)
[INFO]:[core.init_app]: rid=f050ef7cdf985029 start request path=/docs (2023-10-10 18:25:11; init_app.py:44)
[INFO]:[core.init_app]: rid=f050ef7cdf985029 completed_in=0.56ms status_code=200 (2023-10-10 18:25:11; init_app.py:51)
[INFO]:[core.init_app]: rid=9cecea341961c4d3 start request path=/openapi.json (2023-10-10 18:25:11; init_app.py:44)
[INFO]:[core.init_app]: rid=9cecea341961c4d3 completed_in=16.24ms status_code=200 (2023-10-10 18:25:11; init_app.py:51)
```

### Model sql util
By python model output table sql
python ./core/utils/tortoise_util/get_db_sql.py
```
class TestTable(BaseDBModel, BaseCreatedUpdatedAtModel):
    name =fields.CharField(max_length=10)
    age = fields.IntField()

    def __str__(self):
        return self.name

    class Meta:
        table = 'test_table'
```
```sql
CREATE TABLE "test_table" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(10) NOT NULL,
    "age" INT NOT NULL
);
```

### Celery
celery beat 

celery task