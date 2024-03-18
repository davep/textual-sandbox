"""Example of an alternative to table."""

from rich.table import Table
from textual.app import App, ComposeResult
from textual.widgets import OptionList
from textual.widgets.option_list import Option


class DataRow(Option):
    @staticmethod
    def as_row(row_num: int, name_thing: str, some_value: float) -> Table:
        row = Table.grid(expand=True)
        row.add_column(no_wrap=True, width=10)
        row.add_column(no_wrap=True, ratio=1)
        row.add_column(no_wrap=True, width=10)
        row.add_row(f"{row_num}", name_thing, f"{some_value:>10.2f}")
        return row

    def __init__(
        self,
        row_num: int,
        name_thing: str,
        some_value: float,
        id: str | None = None,
        disabled: bool = False,
    ) -> None:
        super().__init__(self.as_row(row_num, name_thing, some_value), id, disabled)


class AltTableApp(App[None]):
    CSS = """
    OptionList {
        scrollbar-gutter: stable;
    }
    """

    def compose(self) -> ComposeResult:
        yield OptionList(*(DataRow(n, "A" * n, n / 100.0) for n in range(1_000)))


if __name__ == "__main__":
    AltTableApp().run()

### alt_table.py ends here
