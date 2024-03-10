import os
import json

PATH = "subjects"


def check(func) -> None:
    if not os.path.exists(PATH):
        os.mkdir(PATH)
    return func


@check
def subject_list() -> list[str]:
    return os.listdir(PATH)


@check
def subject_exist(subject: str) -> bool:
    return os.path.isfile(PATH + "/" + subject)


@check
def create_subject(subject: str, nums: int) -> None:
    with open(PATH + "/" + subject, "w", encoding="utf-8") as file:
        file.write(json.dumps({"favorite": [],
                               "numbers": dict([(i + 1, False) for i in range(nums)])
                               }, indent=2))


@check
def subject_info(subject: str) -> dict:
    ...
