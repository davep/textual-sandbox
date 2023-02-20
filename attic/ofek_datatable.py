"""https://github.com/Textualize/textual/discussions/1820"""

from textual.app import App
from textual.containers import Horizontal, Vertical
from textual.widgets import DataTable, Footer, Header, Label, Switch

class Listing(DataTable):
    def on_mount(self):
        super().on_mount()

        self.add_columns('foo', 'bar')
        self.add_row('a', 'b')

class MyApp(App):
    DEFAULT_CSS = """
    Vertical {
        width: 100%;
    }

    Horizontal {
        width: 100%;
        align: center middle;
    }

    DataTable {
        background: $boost;
        border: round #444;
        width: 50%;
    }
    """

    def compose(self):
        yield Header()
        yield Vertical(
            Horizontal(Switch()),
            Horizontal(Label(''.join(map(str, range(10))))),
            Horizontal(Listing()),
        )
        yield Footer()

if __name__ == '__main__':
    app = MyApp()
    app.run()

