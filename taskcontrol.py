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


class TaskControl():
    def __init__(self, current_subject=None, is_running=False) -> None:
        self.current_subject = current_subject
        self.is_running = is_running

        self.main()
    
    def main(self) -> None:
        while True:
            path = GLOBAL_NAME if not self.current_subject else self.current_subject.name
            text = f"{PROGRAM_NAME}:[{NAME_SUBJ_STYLE}]{path}[/{NAME_SUBJ_STYLE}]$ "
            show(text, end="")
            self.commands = input().split()
            if len(self.commands) == 0:
                continue
            if not self.current_subject:  # global
                match self.commands[0]:
                    case "create":
                        self._create_command()
                    case "choice":
                        self._choice_command()
                    case "list":
                        self._list_command()
                    case "help":
                        self._help_command()
                    case "exit":
                        exit(0)
                    case _:
                        show(INPUT_ERROR)
            else:  # local
                match self.commands[0]:
                    case "help":
                        self._help_command()
                    case "done":
                        self._done_command()
                    case "fav":
                        self._fav_command()
                    case "delfav":
                        self._del_fav_command()
                    case "rand":
                        self._rand_command()
                    case "info":
                        self._info_command()
                    case "rename":
                        self._rename_command()
                    case "gogo":
                        self._gogo_command()
                    case "exit":
                        if "~~" in self.commands[1:]:
                            exit(0)
                        self.current_subject = None
                    case _:
                        show(INPUT_ERROR)

    def _help_command(self) -> None:
        if not self.current_subject:
            show(GLOBAL_HELP_TEXT)
        else:
            show(LOCAL_HELP_TEXT)


    def _create_command(self) -> None:
        if len(self.commands) < 2:
            show(NOT_ARGS_ERROR)
        elif len(self.commands) == 2:
            if not subject_exist(self.commands[1]):
                create_subject(self.commands[1])
            else:
                show(ITEM_EXIST_ERROR)
        else:
            if not subject_exist(self.commands[1]):
                try:
                    create_subject(self.commands[1], int(self.commands[2]))
                except ValueError:
                    show(ARGS_ERROR)
            else:
                show(ITEM_EXIST_ERROR)


    def _choice_command(self) -> None:
        if len(self.commands) < 2:
            show(NOT_ARGS_ERROR)
        else:
            if subject_exist(self.commands[1]):
                self.current_subject = open_subject(self.commands[1])
            else:
                show(NOT_FOUND_ERROR)


    def _list_command(self) -> None:
        show(*subject_list(), sep=SEPARATOR)


    def _fav_command(self) -> None:
        if len(self.commands) > 1:
            try:
                if self.current_subject.numbering:
                    self.current_subject.add_to_fav(*map(int, self.commands[1:]))
                else:
                    self.current_subject.add_to_fav(self.commands[1:])
            except ValueError:
                show(ARGS_ERROR)
        else:
            show(*self.current_subject.favorite, sep=SEPARATOR)


    def _del_fav_command(self) -> None:
        try:
            if self.current_subject.numbering:
                self.current_subject.del_fav(*map(int, self.commands[1:]))
            else:
                self.current_subject.del_fav(self.commands[1:])
        except ValueError:
            show(ARGS_ERROR)


    def _done_command(self) -> None:
        if len(self.commands) > 1:
            try:
                if self.current_subject.numbering:
                    self.current_subject.add_to_done(*map(int, self.commands[1:]))
                else:
                    self.current_subject.add_to_done(*self.commands[1:])
            except ValueError:
                show(ARGS_ERROR)
        else:
            for number in self.current_subject.solved[-QUANTITY_OUTPUT_DONE_CMD:]:
                tm = strftime(TIME_FORMAT_D, localtime(number[1]))
                show(f"[{tm}]{SEPARATOR}{number[0]}")


    def _rand_command(self) -> None:
        try:
            commands = self.commands[1:]
            num1 = num2 = None
            quantity = 1
            for cmd in commands:
                if ".." in cmd:
                    nums = cmd.split("..")
                    if len(nums[0]) != 0:
                        num1 = int(nums[0])
                    if len(nums[1]) != 0:
                        num2 = int(nums[1])
                else:
                    quantity = int(cmd)
            if num1 and num2 and num1 > num2:
                raise ValueError
            randint = self.current_subject.rand_tasks(quantity, num1, num2)
            if randint is None:
                show(NOT_NUMBERING_WARNING)
            elif not randint:
                show(TASKS_SOLVED_MESSAGE)
            else:
                show(*map(str, randint), sep=SEPARATOR)
        except ValueError:
            show(ARGS_ERROR)


    def _info_command(self) -> None:
        if len(self.commands) < 2:
            percent = len(self.current_subject.solved) / self.current_subject.quantity * 100 \
                if self.current_subject.quantity \
                else 100
            num_quantity = {}
            tasks = self.current_subject.solved
            decision_end = None if not tasks else tasks[-1][1] 
            for task in tasks:
                date_str = strftime("%d-%m-%y", localtime(task[1]))
                if date_str not in num_quantity.keys():
                    num_quantity[date_str] = 1
                else:
                    num_quantity[date_str] += 1
            show(INFO.format(
                self.current_subject.name,
                YES if self.current_subject.numbering else NO,
                len(self.current_subject.favorite),
                len(self.current_subject.solved),
                self.current_subject.quantity,
                round(percent, 1),
                sum(num_quantity.values()) // len(num_quantity.values()) if num_quantity else "0",
                max(num_quantity.values()) if num_quantity else "0",
                strftime(TIME_FORMAT_D, localtime(decision_end)) if decision_end else "-",
                round(self.current_subject.time / 3600, 1)
            ))
        else:
            try:
                if self.current_subject.numbering:
                    numbers = list(map(int, self.commands[1:]))
                    print(numbers)
                else:
                    numbers = self.commands[1:]
                for number in numbers:
                    if not self.current_subject.numbering or 0 < number <= self.current_subject.quantity:
                        time_n = None
                        found = False
                        for num, tm in self.current_subject.solved:
                            if num == number:
                                found = True
                                time_n = tm
                                break
                        show(INFO_TASK.format(
                            number,
                            YES if found else NO,
                            YES if number in self.current_subject.favorite else NO,
                            NO if not found else strftime(TIME_FORMAT_D, localtime(time_n))
                        ))
                    else:
                        raise ValueError
            except ValueError:
                show(ARGS_ERROR)


    def _rename_command(self) -> None:
        if len(self.commands) > 2:
            name = " ".join(self.commands[2:])
            match self.commands[1]:
                case "--name" | "-n":
                    self.current_subject.rename(name=name, is_public=True)
                case "--file" | "-f":
                    self.current_subject.rename(name=name, is_public=False)
                case _:
                    show(ARGS_ERROR)
        else:
            show(NOT_ARGS_ERROR)


    def _gogo_command(self) -> None:
        if self.is_running:
            show(ALREADY_RUN_ERROR)
            return

        def run_cmd(cmd: str, file_name: str) -> None:
            self.is_running = True
            process = subprocess.Popen(
                [cmd, file_name],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                stdin=subprocess.DEVNULL
            )
            process.wait()
            self.is_running = False

        root_path = abspath(os.path.dirname(os.path.realpath(__file__)) + "/../") + "/"
        if not os.path.isdir(root_path + self.current_subject.name):
            os.mkdir(root_path + self.current_subject.name)
        name = root_path + self.current_subject.name + "/" + strftime(TIME_FORMAT_F, localtime()) + TYPE
        Thread(target=run_cmd, kwargs=dict(cmd=COMMAND, file_name=name)).start()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and subject_exist(sys.argv[1]):
        current_subject = open_subject(sys.argv[1])
    
    app = TaskControl(current_subject, is_running)
