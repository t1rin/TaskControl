import os

PATH = "subjects"

def check(func) -> None:
    if not os.path.exists(PATH):
        os.mkdir(PATH)
    return func


@check
def subject_list() -> list[str]:
    return os.listdir(PATH)



