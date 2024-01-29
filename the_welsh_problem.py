"""Trying to recreate a rendering bug.

See https://github.com/Textualize/textual/issues/4073
"""

from rich.table import Table
from rich.console import Group

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import OptionList

NAMES = [
    "Cardiff",
    "Swansea",
    "Aberdare",
    "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch",
    "Llanfair­pwllgwyngyll­gogery­chwyrn­drobwll­llan­tysilio­gogo­goch",
    "Mountain Ash",
    "Hirwaun"
]

class Names(ModalScreen[None]):

    CSS = """
    Names {
        align: center middle;

        Vertical {
            width: auto;
            max-width: 60%;
            height: auto;
            max-height: 80%;
            padding: 1 2 0 2;
            background: $surface;
            border: panel $primary;
            border-title-color: $accent;

            OptionList {
                height: 1fr;
                margin: 1 0 1 0;
                &> .option-list--option {
                    padding: 0 5 1 0;
                }
            }
        }
    }
    """

    def gridify(self, n: int, name: str) -> Group:
        question = Table.grid()
        question.add_column(width=3, justify="right")
        question.add_column(width=1)
        question.add_column(ratio=1)
        question.add_row(str(n), "", f"{name} is the name of a place in Wales." )
        answer = Table.grid()
        answer.add_column(width=4)
        answer.add_column(ratio=1)
        answer.add_row("", "[red]Here is the[/] [green]second line[/]")
        return Group(question, answer)

    def compose(self) -> ComposeResult:
        with Vertical():
            yield OptionList(*[self.gridify(n, name) for n, name in enumerate(NAMES)])

class TruncatedTextOptionApp(App[None]):

    CSS = """
    Screen#_default {
        background: red;
    }
    """

    def on_mount(self) -> None:
        self.push_screen(Names())

if __name__ == "__main__":
    TruncatedTextOptionApp().run()

### the_welsh_problem.py ends here
