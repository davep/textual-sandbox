"""https://discord.com/channels/1026214085173461072/1033754296224841768/1137548723581366442"""

from textual.widgets import DataTable
from textual.app import ComposeResult, App


class My_App(App):

    ROWS = [
        ("lane", "swimmer", "country", "time"),
        (4, "Joseph Schooling", "Singapore", 50.39),
        (2, "Michael Phelps", "United States", 51.14),
        (5, "Chad le Clos", "South Africa", 51.14),
        (6, "László Cseh", "Hungary", 51.14),
        (3, "Li Zhuhao", "China", 51.26),
        (8, "Mehdy Metella", "France", 51.58),
        (7, "Tom Shields", "United States", 51.73),
        (1, "Aleksandr Sadovnikov", "Russia", 51.84),
        (10, "Darren Burns", "Scotland", 51.84),
    ]

    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*My_App.ROWS[0])
        table.add_rows(My_App.ROWS[1:])

    def on_key(self) -> None:
        table = self.query_one(DataTable)
        print(table.cursor_coordinate)


if __name__ == "__main__":
    app = My_App()
    app.run()
