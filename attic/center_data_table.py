"""https://github.com/Textualize/textual/issues/1442#issuecomment-1375070241"""

import csv
import io

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable

CSV = """lane,swimmer,country,time
4,Joseph Schooling,Singapore,50.39
2,Michael Phelps,United States,51.14
5,Chad le Clos,South Africa,51.14
6,László Cseh,Hungary,51.14
3,Li Zhuhao,China,51.26
8,Mehdy Metella,France,51.58
7,Tom Shields,United States,51.73
1,Aleksandr Sadovnikov,Russia,51.84"""


class CenterDataTable(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }

    DataTable {
        width: 40%;
        height: 40%;
        border: round red;
    }

    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield DataTable[str]()
        yield Footer()

    def on_mount(self) -> None:
        """"""
        table = self.query_one(DataTable[str])
        rows = csv.reader(io.StringIO(CSV))
        table.add_columns(*next(rows))
        table.add_rows(rows)


if __name__ == "__main__":
    CenterDataTable().run()
