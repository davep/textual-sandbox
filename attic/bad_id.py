"""Bad ID tester.

https://github.com/Textualize/textual/issues/659
"""

from textual.app import App
from textual.widgets import Button


class IDTester(App[None]):

    CSS = """
    Button { width: 100%; height: 100%; }
    """

    BAD_ID = "1-button"

    def compose(self):
        yield Button("Push Me", id=self.BAD_ID)

    def handle_pressed(self, event):
        _ = self.query(f"#{self.BAD_ID}")


if __name__ == "__main__":
    IDTester().run()

