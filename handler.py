import re

from rich import print

styles = {
    "default": "white",  # default
    "h1": "bold green",  # program name style
    "h2": "bold yellow",  # arguments
    "h3": "white underline",  # headings
    "h4": "bold blue",  # name subject style
    "h5": "bold",  # important words
    "cmd": "green",  # command
    "comment": "italic gray70",  # comments
    "warning": "white"  # warning messages
}


def _format_text(match) -> str:
    name = match.group(1)
    text = match.group(2)
    if name in styles.keys():
        style = styles[name]
    else:
        # style = styles["default"]
        style = name
    return f"[{style}]{text}[/]"


def format_text(text: str) -> str:
    pattern = r"\[(.*?)\](.*?)\[/\1\]"
    return re.sub(pattern, _format_text, text)


def show(*args, **kwargs) -> None:
    result = [format_text(arg) if isinstance(arg, str) else arg for arg in args]
    print(*result, **kwargs)
