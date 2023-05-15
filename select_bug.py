from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Select, Button


class SelectBug(App):

    def compose(self) -> ComposeResult:
        self.select = Select(options=[("empty", 0)])
        yield self.select
        yield Button("Change Options", id="change_options")

    @on(Button.Pressed, "#change_options")
    def change_options(self, event):
        self.select.set_options([("Four", 4), ("Five", 5), ("Six", 6)])


if __name__ == "__main__":
    app = SelectBug()
    app.run()

