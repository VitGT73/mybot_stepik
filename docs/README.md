
***Poetry***


если мы добавляем Poetry в новый проект:
```shell
poetry init
```
для первичной установки
```shell
poetry install
```

для обновления всех пакетов:
```shell
poetry update
```

или только одного пакета:

```shell
poetry update pygame
```

Чтобы добавить новую библиотеку достаточно выполнить:

```
poetry add pygame
```

Чтобы удалить зависимость достаточно выполнить:
```shell
poetry remove pygame
```

Чтобы посмотреть зависимости проекта:

```shell
poetry show
```

Посмотреть дерево зависимостей проекта можно при помощи:

```shell
poetry show --tree
```

Чтобы Poetry создавал виртуальное окружение не в cache-директории, 
а в корневом каталоге проекта. Для этого установим переменной 
virtualenvs.in-project  значение true:
```shell
poetry config virtualenvs.in-project true
```

Чтобы убедиться, что значение успешно установилась, выполним команду:
```shell
poetry config virtualenvs.in-project
```

Чтобы посмотреть все текущие параметры Poetry, используйте команду:
```shell
poetry config --list
```

Если параметр нужно удалить, используйте флаг `--unset`:
```shell
poetry config virtualenvs.in-project --unset
```
