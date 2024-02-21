"""https://github.com/Textualize/textual/discussions/3328"""

from random import randint, random

from textual.app import App, ComposeResult
from textual.widgets import DataTable


class UpdatingTableExampleApp(App[None]):

    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:

        table = self.query_one(DataTable)
        table.add_column("Parameter", key="param")
        table.add_column("Value", key="value")
        for n in range(50):
            table.add_row(f"Paramater {n}", 0, key=f"param{n}")

        self.set_interval(0.1, self.update_table)

    def update_table(self) -> None:
        table = self.query_one(DataTable)
        row = randint(0, 49)
        table.update_cell(f"param{row}", "value", random())


if __name__ == "__main__":
    UpdatingTableExampleApp().run()
