# TaskControl

Assistant program for tracking the completion of assignments in subjects

Further, in Russian >>

Программа для контроля выполнения заданий по предметам.
Теперь вы сможете решить все номера какого-нибудь сборника задач, с контролем прогресса

## Запуск

В аргумент запуска можно передать имя уже существующего предмета

```shell
python3 taskcontrol.py
```

## Команды

### Глобальные

`create NAME NUMBERS` создает новый предмет с названием NAME и количеством номеров заданий NUMBERS

`choice NAME` выбирает существующий предмет с названием NAME

`list` возвращает все существующие предметы

`help` возвращает справку по командам

`exit` закрывает программу

### Локальные

_**Локальные команды** - команды для работы с отдельными предметами. **Работают, если выбран предмет**_

`done [1 номер] [2 номер] ... [n номер]` вносит в базу указанные номера, как выполненные

`fav [1 номер] [2 номер] ... [n номер]` вносит в базу указанные номера, как избранные

`rand N` возвращает N случайных номеров из нерешенных

`info` возвращает общие сведения о выполненных заданиях

`help` возвращает справку по командам

`exit` выходит в глобальную среду
