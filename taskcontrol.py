from subject import *
from handler import *
from config import *

from time import strftime, localtime
from threading import Thread
from os.path import abspath
import subprocess
import os

current_subject: Subject | None = None
is_running: bool = False


def _help_command() -> None:
    if not current_subject:
        show(GLOBAL_HELP_TEXT)
    else:
        show(LOCAL_HELP_TEXT)


def _create_command(commands: list[str]) -> None:
    if len(commands) < 3:
        show(NOT_ARGS_ERROR)
    else:
        if not subject_exist(commands[1]):
            try:
                create_subject(commands[1], int(commands[2]))
            except ValueError:
                show(ARGS_ERROR)
        else:
            show(ITEM_EXIST_ERROR)


def _choice_command(commands: list[str]) -> None:
    if len(commands) < 2:
        show(NOT_ARGS_ERROR)
    else:
        if subject_exist(commands[1]):
            global current_subject
            current_subject = open_subject(commands[1])
        else:
            show(NOT_FOUND_ERROR)


def _list_command() -> None:
    show(*subject_list(), sep=SEPARATOR)


def _fav_command(commands: list[str]) -> None:
    if len(commands) > 1:
        try:
            current_subject.add_to_fav(*map(int, commands[1:]))
        except ValueError:
            show(ARGS_ERROR)
    else:
        show(*current_subject.favorite, sep=SEPARATOR)


def _del_fav_command(commands: list[str]) -> None:
    try:
        current_subject.del_fav(*map(int, commands[1:]))
    except ValueError:
        show(ARGS_ERROR)


def _done_command(commands: list[str]) -> None:
    if len(commands) > 1:
        try:
            current_subject.add_to_done(*map(int, commands[1:]))
        except ValueError:
            show(ARGS_ERROR)
    else:
        for number in current_subject.solved:
            tm = strftime(TIME_FORMAT_D, localtime(number[1]))
            show(f"[{tm}]{SEPARATOR}{number[0]}")


def _rand_command(commands: list[str]) -> None:
    if len(commands) < 2:
        show(NOT_ARGS_ERROR)
    else:
        try:
            quantity = int(commands[1])
            show(*map(str, current_subject.rand_tasks(quantity)), sep=SEPARATOR)
        except ValueError:
            show(ARGS_ERROR)


def _info_command(commands: list[str]) -> None:
    if len(commands) < 2:
        percent = len(current_subject.solved) / current_subject.quantity * 100
        num_quantity = {}
        tasks = current_subject.solved
        decision_end = None if not tasks else tasks[-1][1] 
        for task in tasks:
            date_str = strftime("%d-%m-%y", localtime(task[1]))
            if date_str not in num_quantity.keys():
                num_quantity[date_str] = 1
            else:
                num_quantity[date_str] += 1
        show(INFO.format(
            current_subject.name,
            len(current_subject.favorite),
            len(current_subject.solved),
            current_subject.quantity,
            round(percent, 1),
            sum(num_quantity.values()) // len(num_quantity.values()) if num_quantity else "0",
            max(num_quantity.values()) if num_quantity else "0",
            strftime(TIME_FORMAT_D, localtime(decision_end)),
            round(current_subject.time / 3600, 1)
        ))
    else:
        try:
            number = int(commands[1])
            if 0 < number <= current_subject.quantity:
                time_n = None
                found = False
                for num, tm in current_subject.solved:
                    if num == number:
                        found = True
                        time_n = tm
                        break
                show(INFO_TASK.format(
                    number,
                    YES if found else NO,
                    YES if number in current_subject.favorite else NO,
                    NO if not found else strftime(TIME_FORMAT_D, localtime(time_n))
                ))
            else:
                raise ValueError
        except ValueError:
            show(ARGS_ERROR)


def _rename_command(commands: list[str]) -> None:
    if len(commands) > 2:
        name = commands[2]
        match commands[1]:
            case "--file" | "-f":
                current_subject.rename(name=name, is_public=True)
            case "--code" | "-c":
                current_subject.rename(name=name, is_public=False)
            case _:
                show(ARGS_ERROR)
    else:
        show(NOT_ARGS_ERROR)


def _gogo_command() -> None:
    global is_running
    if is_running:
        show(ALREADY_RUN_ERROR)
        return

    def run_cmd(cmd: str, file_name: str) -> None:
        global is_running
        is_running = True
        process = subprocess.Popen(
            [cmd, file_name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL
        )
        process.wait()
        is_running = False

    root_path = abspath(os.path.dirname(os.path.realpath(__file__)) + "/../") + "/"
    if not os.path.isdir(root_path + current_subject.name):
        os.mkdir(root_path + current_subject.name)
    name = root_path + current_subject.name + "/" + strftime(TIME_FORMAT_F, localtime())
    Thread(target=run_cmd, kwargs=dict(cmd=COMMAND, file_name=name)).start()


def main() -> None:
    global current_subject
    while True:
        path = GLOBAL_NAME if not current_subject else current_subject.name
        text = f"{PROGRAM_NAME}:[{NAME_SUBJ_STYLE}]{path}[/{NAME_SUBJ_STYLE}]$ "
        show(text, end="")
        commands = input().split()
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
                    show(INPUT_ERROR)
        else:  # local
            match commands[0]:
                case "help":
                    _help_command()
                case "done":
                    _done_command(commands)
                case "fav":
                    _fav_command(commands)
                case "delfav":
                    _del_fav_command(commands)
                case "rand":
                    _rand_command(commands)
                case "info":
                    _info_command(commands)
                case "rename":
                    _rename_command(commands)
                case "gogo":
                    _gogo_command()
                case "exit":
                    current_subject = None
                case _:
                    show(INPUT_ERROR)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and subject_exist(sys.argv[1]):
        current_subject = open_subject(sys.argv[1])
    main()
