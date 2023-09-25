Generic single-database configuration with an async dbapi.

Установка Alembic:

```console
poetry add alembic
```


Конфигурация сгенерированная с помощью команды:

```console
alembic init -t async alembic
```



Для сортировки миграций в хронологическом порядке раскомментируем в файле `alembic.ini` строчку:
`# file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s`


Подключаем модели из приложения и Читаем конфигурацию Алхимии и модели.
Добавляем в `env.py` вместо `# target_metadata = None` следующие строки:

```python
from core.models import Base
from core import config

target_metadata = Base.metadata
config.set_main_option("sqlalchemy.url", config.sql_url)
```

Создаем первый ревижн таблицы:
```concole
alembic revision --autogenerate -m "Create first tables"
```

Подключаем **black**  файле `alembic.ini`, для этого раскомментируем строки:
```config
 hooks = black
 black.type = console_scripts
 black.entrypoint = black
 black.options = -l 79 REVISION_SCRIPT_FILENAME
```

Обновляемся до первой миграции:

```console
alembic upgrade head
```

Откатится на один шаг назад:
```shell
alembic downgrade -1
```

