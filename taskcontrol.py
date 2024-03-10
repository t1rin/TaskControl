from subject import *
from config import *

current_subject = None


def input_error() -> None:
    print(INPUT_ERROR_TEXT)


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
                case "list":
                    for subject in subject_list():
                        print(subject)
                case "help":
                    _command_help()
                case "exit":
                    exit(0)
                case _:
                    input_error()
        else:  # local
            match commands[0]:
                case "exit":
                    current_subject = None
                case _:
                    input_error()


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        current_subject = sys.argv[1]
    main()
