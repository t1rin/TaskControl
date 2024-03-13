GLOBAL_HELP_TEXT = """
global commands:
  create [NAME] [NUMBERS] создает новый предмет с названием NAME и количеством номеров заданий NUMBERS
  choose [NAME] выбирает существующий предмет с названием NAME
  list возвращает все существующие предметы
  help возвращает то, что вы сейчас читаете
  exit закрывает программу
"""

LOCAL_HELP_TEXT = """
local commands:
  help возвращает то, что вы сейчас читаете
  exit выходит в глобальную среду
"""

PROGRAM_NAME = "taskcontrol-command"

GLOBAL_NAME = "~"

INPUT_ERROR_TEXT = "Команда не найдена. help для получения дополнительной информации"

ZERO_LIST_TEXT = "Вы ещё не создали ни одного предмета"

NOT_ARGS_ERROR = "Недостаточно аргументов"

ARGS_ERROR = "Не подходящие аргументы"

NOT_FOUND_ERROR = "Указанного предмета не существует"

ITEM_EXIST_ERROR = "Предмет уже существует"