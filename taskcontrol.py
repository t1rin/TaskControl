from subject import *
from config import *

current_subject = None


def _command_help() -> None:
    if not current_subject:
        print(GLOBAL_HELP_TEXT)
    else:
        print(LOCAL_HELP_TEXT)


def main() -> None:
    global current_subject
    while True:
        commands = input(PROGRAM_NAME + ":" + (current_subject if current_subject else GLOBAL_NAME) + "$ ").split()
        if len(commands) == 0:
            continue
        if not current_subject:  # global
            match commands[0]:
                case "create":
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
                case "choose":
                    if len(commands) < 2:
                        print(NOT_ARGS_ERROR)
                    else:
                        if subject_exist(commands[1]):
                            current_subject = commands[1]
                        else:
                            print(NOT_FOUND_ERROR)
                case "list":
                    subjects = subject_list()
                    for subject in subjects:
                        print(subject)
                    if len(subjects) == 0:
                        print(ZERO_LIST_TEXT)
                case "help":
                    _command_help()
                case "exit":
                    exit(0)
                case _:
                    print(INPUT_ERROR)
        else:  # local
            match commands[0]:
                case "help":
                    _command_help()
                case "exit":
                    current_subject = None
                case _:
                    print(INPUT_ERROR)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        current_subject = sys.argv[1]
    main()
