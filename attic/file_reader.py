from pathlib import Path

from textual import work
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Log, Footer


class ShowFile(Screen):

    def __init__(self, path: Path, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.path = path

    def on_mount(self) -> None:
        self.sub_title = f"Showing: {self.path.name}"
        self.read_file(self.path)

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Log(classes="status-richlog")
        yield Footer()

    @work(thread=True)
    def read_file(self, path: Path) -> None:
        log = self.query_one(Log)
        with open(path, "r") as f:
            for line in f:
                self.app.call_from_thread(log.write, line)


class LoadUpFileApp(App[None]):

    def on_mount(self) -> None:
        self.push_screen(ShowFile(Path(__file__)))


if __name__ == "__main__":
    LoadUpFileApp().run()

### file_reader.py ends here
