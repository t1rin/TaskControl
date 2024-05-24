GLOBAL_HELP_TEXT = """
[h3]global commands:[/h3]
  [cmd]create[/cmd] ([h2]<NAME> <NUMBERS>[/h2] | [h2]<NAME>[/h2]) создает новый предмет с названием [h2]NAME[/h2] и количеством номеров заданий [h2]NUMBERS[/h2]
  [cmd]choice[/cmd] [h2]<NAME>[/h2] выбирает существующий предмет с названием [h2]NAME[/h2]
  [cmd]list[/cmd] возвращает все существующие предметы
  [cmd]help[/cmd] возвращает то, что вы сейчас читаете
  [cmd]exit[/cmd] закрывает программу
"""

LOCAL_HELP_TEXT = """
[h3]local commands:[/h3]
  [cmd]help[/cmd] возвращает то, что вы сейчас читаете
  [cmd]done[/cmd] [h2]\[1 номер] \[2 номер] ... \[n номер][/h2] вносит в базу выполненных задач указанные номера;
    без аргументов возвращает список выполненных задач
  [cmd]fav[/cmd] [h2]\[1 номер] \[2 номер] ... \[n номер][/h2] вносит в базу избранных задач указанные номера;
    без аргументов возвращает список избранных задач
  [cmd]delfav[/cmd] [h2]\[1 номер] \[2 номер] ... \[n номер][/h2] удаляет из базы избранных задач указанные номера
  [cmd]rand[/cmd] [h2]\[N][/h2] [h2]\[\[n1]..\[n2]][/h2] если нумерация номеров присутствует, возвращает [h2]N[/h2] случайных номеров из нерешенных в диапозоне от [h2]n1[/h2] до [h2]n2[/h2]
  [cmd]gogo[/cmd] выполняет команду из [i]config.py[/i] с аргуметом названия предмета и даты; предусматривается для открытия редактора, и решения задачь в нём
  [cmd]info[/cmd] [h2]\[номер][/h2] если номер не указан, возвращает общие сведения о выполненных заданиях, иначе о номере
  [cmd]rename[/cmd] [h2]<--name | --file>[/h2] переименовывает название предмета, если флаг [h2]--name[/h2], иначе, если флаг [h2]--file[/h2], переименовывает название файла предмета
  [cmd]exit[/cmd] выходит в глобальную среду
"""

INFO = """
[h5]Название предмета[/h5]: [h3]{}[/h3]

Задания нумеруются: {}

[h5]Задания[/h5]:
- [h2]{}[/h2] в [italic]избранном[/italic]
- [h2]{}[/h2]/[h2]{} {}[/h2]% выполнено

[h5]В среднем[/h5] [h2]{}[/h2] [h5]задача/день[/h5]
[h5]Максимальное количество задача/день:[/h5] [h2]{}[/h2]
[h5]Последнее решение:[/h5] [h2]{}[/h2]
[h5]Количество часов на предмете:[/h5] [h2]{}[/h2]
"""

INFO_TASK = """
[h5]Номер задачи[/h5]: {}
[h5]Выполнено[/h5]: {}
[h5]Есть в избранном[/h5]: {}
[h5]Когда решена[/h5]? {}
"""

PROGRAM_NAME = "[h1]taskcontrol-command[/h1]"

GLOBAL_NAME = "~"

NAME_SUBJ_STYLE = "h4"

SEPARATOR = "    "

YES = "[bold yellow]Да[/bold yellow]"  # ":+1:"

NO = "[bold yellow]Нет[/bold yellow]"  # ":-1:"

TIME_FORMAT_D = "%d-%m-%y %H:%M"

TIME_FORMAT_F = "Задачи-%d-%m-%y"

COMMAND = "xournalpp"  # :)

TYPE = ".xopp"

INPUT_ERROR = "[warning]Команда не найдена.[/warning] help [warning]для получения дополнительной информации[/warning]"

ZERO_LIST_TEXT = "[warning]Вы ещё не создали ни одного предмета[/warning]"

NOT_ARGS_ERROR = "[warning]Недостаточно аргументов[/warning]"

ARGS_ERROR = "[warning]Не подходящие аргументы[/warning]"

NOT_FOUND_ERROR = "[warning]Указанного предмета не существует[/warning]"

ITEM_EXIST_ERROR = "[warning]Предмет уже существует[/warning]"

ALREADY_RUN_ERROR = "[warning]Программа не завершила свое работу[/warning]"

NOT_NUMBERING_WARNING = "[warning]Задачи не нумеруются[/warning]"

TASKS_SOLVED_MESSAGE = "[message]Нерешённых задач не найдено[/message]"
