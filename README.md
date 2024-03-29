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

## Структура

`.TaskControl/`<br>
├── `taskcontrol.py` - главный файл<br>
├── `subject.py` - файл для работы с предметами<br>
├── `handler.py` - файл для обработки выводимого текста<br>
└── `config.py` - файл конфигурации<br>

## Команды

### Глобальные

`create <NAME> <NUMBERS>` создает новый предмет с названием NAME и количеством номеров заданий NUMBERS

`choice <NAME>` выбирает существующий предмет с названием NAME

`list` возвращает все существующие предметы

`help` возвращает справку по командам

`exit` закрывает программу

### Локальные

_**Локальные команды** - команды для работы с отдельными предметами. **Работают, если выбран предмет**_

`done [1 номер] [2 номер] ... [n номер]` вносит в базу выполненных задач указанные номера;
    без аргументов возвращает список выполненных задач

`fav [1 номер] [2 номер] ... [n номер]` вносит в базу избранных задач указанные номера;
    без аргументов возвращает список избранных задач

`rand <K>` возвращает K случайных номеров из нерешенных

`info [номер]` если номер не указан, возвращает общие сведения о выполненных заданиях, иначе о номере

`rename <--file | --code>` переименовывает название предмета, если флаг --file, иначе, если флаг --code, переименовывает название, используемое в программе

`gogo` выполняет команду из _config.py_ с аргуметом названия предмета и даты; предусматривается для открытия редактора, и решения задачь в нём

`help` возвращает справку по командам

`exit` выход в глобальную среду

## _Примечание_

Программу решили разработать для увлекательной подготовки к олимпиадам, экзаменам и для решения различных задач.


Папку `.TaskControl` с кодом можно поместить в папку с именем, например, `Задачи`... 
А в папке `Задачи`, кроме папки с кодом, находятся папки предметов, 
в которых подразумевается хранить решения задач

`Задачи/`<br>
├ `.TaskControl/`<br>
│   ├ `subject/`<br>
│   │   └ `<данные о предметах>`<br>
│   └─ `<файлы программы>`<br>
├ `<subject name>`<br>
│   └─ `<файлы решений>`<br>
└─ `<другие предметов>`<br>

Чтобы удобно добавлять файлы решений,
добавлена команда `gogo`

Чтобы воспользоваться этим функционалом, 
нужно заменить в конфиге значение переменной `COMMAND` на свою программу для решения задач

Для программы с именем `texteditor` и названием файла решения `PATH/task-00-00-00` за счет команды `gogo` в терминале запуститься
```shell
texteditor PATH/task-00-00-00
```
