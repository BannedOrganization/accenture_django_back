# angry_lab_backend

### 1
установите python 3.6.7

### 2
git clone

### 3
cd project_name/

### 4
pip install -r requirements36.txt


### 5
делаем копию .env.example и убираем '.example' с конца (получиться файл с именем '.env')

### 6
cd angrylab_dj_bkend
python manage.py shell
```py
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()
```

### 7
dotenv set SECRET_KEY **************************


### 8
установите redis и добавьте его порт в настройки в .env


### 9
Добавить в 
CORS_ALLOWED_ORIGINS
адрес второго сервиса
```py
CORS_ALLOWED_ORIGINS = [
    'https://somesite.com/'
]

```

### 10
```py
ALLOWED_HOSTS = ['somesite.com']
```

### 11
подключение celery 
```bash
celery -A angrylab_dj_bkend worker -l info -P gevent
```

### 12
```bash
python manage.py runserver
```