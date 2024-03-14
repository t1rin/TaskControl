from os.path import exists
from os import mkdir, listdir
import json

from json.decoder import JSONDecodeError

PATH = "subjects"


def check(func) -> None:
    if not exists(PATH):
        mkdir(PATH)
    return func


@check
def subject_exist(name: str) -> bool:
    keys = ["name", "quantity", "favorite", "solved"]
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
        print(error)
        exit(1)
    return True


@check
def subject_list() -> list[str]:
    files = listdir(PATH)
    file_list = []
    for file in files:
        if subject_exist(file):
            file_list.append(file)
    return file_list


class Subject:
    """ Класс уже созданных предметов """
    def __init__(self, name) -> None:
        self.name: str = name
        self.quantity: int | None = None
        self._favorite: list[int] | None = None
        self._solved: list[int] | None = None

        self._load_subject()


    def add_to_fav(self, *args) -> None:
        self._favorite.extend(args)
        self._favorite = list(set(self._favorite))
        self._favorite = [n for n in self._favorite if n <= self.quantity]
        self.update()


    def add_to_done(self, *args) -> None:
        self._solved.extend(args)
        self._solved = list(set(self._solved))
        self._solved = [n for n in self._solved if n <= self.quantity]
        self.update()


    def update(self) -> None:
        dictionary = {
            "name": self.name,
            "quantity": self.quantity,
            "favorite": self._favorite,
            "solved": self._solved
        }
        with open(PATH + "/" + self.name, "w", encoding="utf-8") as file:
            file.write(json.dumps(dictionary, indent=2))


    def _load_subject(self) -> None:
        with open(PATH + "/" + self.name, "r", encoding="utf-8") as file:
            dictionary = json.loads(file.read())
            self.name = dictionary["name"]
            self.quantity = dictionary["quantity"]
            self._favorite = dictionary["favorite"]
            self._solved = dictionary["solved"]


def create_subject(name: str, number_of_tasks: int) -> None:
    dictionary = {
        "name": name,
        "quantity": number_of_tasks,
        "favorite": [],
        "solved": []
    }
    with open(PATH + "/" + name, "w", encoding="utf-8") as file:
        file.write(json.dumps(dictionary, indent=2))
