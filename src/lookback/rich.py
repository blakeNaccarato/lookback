"""Initialization for rich.

Avoid activating Rich features that break functionality outside of the REPL.
"""


def init():
    from rich import traceback

    traceback.install()

    if not is_notebook_or_ipython():
        from rich import pretty

        pretty.install()


# https://stackoverflow.com/a/39662359
def is_notebook_or_ipython() -> bool:
    try:
        shell = get_ipython().__class__.__name__  # type: ignore  # Dynamic
    except NameError:
        return False  # Probably standard Python interpreter
    else:
        return shell == "TerminalInteractiveShell"
