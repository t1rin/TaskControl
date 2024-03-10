import sys

from subject import *

current_subject = None


def input_error() -> None:
    ...


def main() -> None:
    while True:
        commands = input("command:" + (current_subject if current_subject else "~") + "$ ").split()
        if not current_subject:  # global
            match commands[0]:
                case "list":
                    ...
                case _:
                    input_error()
        else:  # local
            match commands[0]:
                case "exit":
                    ...
                case _:
                    input_error()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        current_subject = sys.argv[1]
    main()
