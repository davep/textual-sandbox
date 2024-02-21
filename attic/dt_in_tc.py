from textual.app import App
from textual.widgets import DataTable, Label, TabbedContent


DATA = [("anji", 23, "ok@no.com", "somewhere"), ("mike", 32, "no@ok.net", "elsewhere")]


class MyApp(App):

    CSS = """
    DataTable {
       height: 1fr;
    }
    """

    def __init__(self):
        super().__init__()
        self.table = DataTable(id="table", show_header=True)
        self.table.add_columns(*["name", "age", "email", "addr"])
        for row in DATA:
            self.table.add_row(*row)

    def compose(self):
        with TabbedContent("Basic", "Advanced"):
            yield self.table
            yield Label("Here's some advanced stuff", id="label")


if __name__ == "__main__":
    app = MyApp()
    app.run()
