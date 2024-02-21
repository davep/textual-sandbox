"""https://github.com/Textualize/textual/discussions/3535#discussioncomment-7544326"""

from io import TextIOWrapper
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button


class OpenCloseFileApp(App[None]):

    def __init__(self, my_file: TextIOWrapper) -> None:
        super().__init__()
        self.my_file = my_file

    def compose(self) -> ComposeResult:
        yield Button("Write a thing and close me")

    @on(Button.Pressed)
    def write_and_close(self) -> None:
        self.my_file.write("And we're done!\n")
        self.exit()


if __name__ == "__main__":
    with open("foo.txt", "a", encoding="utf-8") as my_file:
        OpenCloseFileApp(my_file).run()

### open_close_file.py ends here
