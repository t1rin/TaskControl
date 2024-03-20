from random import sample

import time
import json
import os

from json.decoder import JSONDecodeError

PATH = os.path.dirname(os.path.realpath(__file__)) + "/subjects"


def subject_exist(name: str) -> bool:
    if not os.path.isdir(PATH):
        os.mkdir(PATH)
    keys = ["name", "quantity", "time", "favorite", "solved"]
    path = PATH + "/" + name
    try:
        with open(path, "r", encoding="utf-8") as file:
            dictionary = json.loads(file.read())
            for key in keys:
                if key not in dictionary:
                    return False
    except FileNotFoundError:
        return False
    except JSONDecodeError as error:
        # print(error)
        return False
    return True


def subject_list() -> list[str]:
    if not os.path.isdir(PATH):
        os.mkdir(PATH)
    files = os.listdir(PATH)
    file_list = []
    for file in files:
        if subject_exist(file):
            file_list.append(file)
    return file_list


class Subject:
    """ Класс уже созданных предметов """
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.name: str | None = None
        self.quantity: int | None = None
        self.time: int | None = None
        self.favorite: list[int] | None = None
        self.solved: list[list[int]] | None = None

        self.timestamp = int(time.time())

        self._load_subject()

    def rand_tasks(self, quantity: int) -> list[int]:
        all_tasks = {i + 1 for i in range(self.quantity)}
        if self.solved:
            solved = list(zip(*self.solved))[0]
        else:
            solved = []
        return sample(list(all_tasks - set(solved)), quantity)

    def rename(self, name: str, is_public: bool) -> None:
        if is_public:
            self.name = name
            self.update()
        else:
            os.rename(PATH + "/" + self.file_name, PATH + "/" + name)
            self.file_name = name

    def add_to_fav(self, *args) -> None:
        self.favorite.extend(args)
        self.favorite = list(set(self.favorite))
        self.favorite = [n for n in self.favorite if n <= self.quantity]
        self.update()

    def del_fav(self, *args) -> None:
        self.favorite = [x for x in self.favorite if x not in args]
        self.update()

    def add_to_done(self, *args) -> None:
        for arg in args:
            solved = list(zip(*self.solved))[0] \
                if self.solved \
                else []
            if arg not in solved and 0 < arg <= self.quantity:
                self.solved.append([arg, int(time.time())])
        self.update()

    def update(self) -> None:
        self.time += int(time.time() - self.timestamp)
        self.timestamp = int(time.time())
        dictionary = {
            "name": self.name,
            "quantity": self.quantity,
            "time": self.time,
            "favorite": self.favorite,
            "solved": self.solved
        }
        with open(PATH + "/" + self.file_name, "w", encoding="utf-8") as file:
            file.write(json.dumps(dictionary, indent=2))

    def _load_subject(self) -> None:
        with open(PATH + "/" + self.file_name, "r", encoding="utf-8") as file:
            dictionary = json.loads(file.read())
            self.name = dictionary["name"]
            self.quantity = dictionary["quantity"]
            self.time = dictionary["time"]
            self.favorite = dictionary["favorite"]
            self.solved = dictionary["solved"]


def create_subject(name: str, number_of_tasks: int) -> None:
    dictionary = {
        "name": name,
        "quantity": number_of_tasks,
        "time": 0,
        "favorite": [],
        "solved": []
    }
    with open(PATH + "/" + name, "w", encoding="utf-8") as file:
        file.write(json.dumps(dictionary, indent=2))


def open_subject(name: str) -> Subject:
    return Subject(name)
