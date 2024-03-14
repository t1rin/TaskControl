from os.path import exists
from os import mkdir, listdir
import json

from json.decoder import JSONDecodeError

PATH = "subjects"
extension = ".json"

def check(func) -> None:
    if not exists(PATH):
        mkdir(PATH)
    return func


@check
def subject_exist(name: str) -> bool:
    keys = ["name", "quantity", "favorite", "solved"]
    path = PATH + "/" + name + extension
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
    def __init__(self, name):
        self.name: str = name
        self.quantity: int | None = None
        self.favorite: list[int] | None = None
        self.solved: list[int] | None = None

        self._load_subject()

    def _load_subject(self):
        with open(PATH + "/" + self.name + extension, "r", encoding="utf-8") as file:
            dictionary = json.loads(file.read())
            self.name = dictionary["name"]
            self.quantity = dictionary["quantity"]
            self.favorite = dictionary["favorite"]
            self.solved = dictionary["solved"]


def create_subject(name: str, number_of_tasks: int) -> None:
    dictionary = {
        "name": name,
        "quantity": number_of_tasks,
        "favorite": [],
        "solved": []
    }
    with open(PATH + "/" + name + extension, "w", encoding="utf-8") as file:
        file.write(json.dumps(dictionary, indent=2))
