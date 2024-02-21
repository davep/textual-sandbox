"""Example of default behaviour."""

from textual.app import App, ComposeResult
from textual.widgets import Static, Log


class Parent(Static):

    def on_mount(self) -> None:
        self.app.query_one(Log).write_line("This is from Parent.on_mount")


class Child(Parent):

    def on_mount(self) -> None:
        self.app.query_one(Log).write_line("This is from Child.on_mount")


class OnMountDefaultApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Child()
        yield Log()


if __name__ == "__main__":
    OnMountDefaultApp().run()

### mount_default.py ends here
