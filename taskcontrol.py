from subject import *
from config import *

current_subject: Subject | None = None


def _help_command() -> None:
    if not current_subject:
        print(GLOBAL_HELP_TEXT)
    else:
        print(LOCAL_HELP_TEXT)


def _create_command(commands) -> None:
    if len(commands) < 3:
        print(NOT_ARGS_ERROR)
    else:
        if not subject_exist(commands[1]):
            try:
                create_subject(commands[1], int(commands[2]))
            except ValueError:
                print(ARGS_ERROR)
        else:
            print(ITEM_EXIST_ERROR)


def _choice_command(commands) -> None:
    if len(commands) < 2:
        print(NOT_ARGS_ERROR)
    else:
        if subject_exist(commands[1]):
            global current_subject
            current_subject = Subject(commands[1])
        else:
            print(NOT_FOUND_ERROR)


def _list_command() -> None:
    print(*subject_list(), sep="    ")


def main() -> None:
    global current_subject
    while True:
        text = PROGRAM_NAME + ":" + (GLOBAL_NAME if not current_subject else current_subject.name) + "$ "
        commands = input(text).split()
        if len(commands) == 0:
            continue
        if not current_subject:  # global
            match commands[0]:
                case "create":
                    _create_command(commands)
                case "choice":
                    _choice_command(commands)
                case "list":
                    _list_command()
                case "help":
                    _help_command()
                case "exit":
                    exit(0)
                case _:
                    print(INPUT_ERROR)
        else:  # local
            match commands[0]:
                case "help":
                    _help_command()
                case "exit":
                    current_subject = None
                case _:
                    print(INPUT_ERROR)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1: #
        current_subject = sys.argv[1]
    main()
