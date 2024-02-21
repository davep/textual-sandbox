"""https://github.com/Textualize/textual/discussions/1321"""

from __future__ import annotations  # noqa

from rich.console import Console
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Label, Footer, Header

console = Console()


class Dialog(Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = Container(
            Label("Example App"),
            Label("A tool for doing something or other"),
            Label("Copyright (C) 2022 The Copyright Holders"),
            Label("https://www.example.com/"),
            id="dialog",
        )

    def compose(self) -> ComposeResult:
        yield self.content


DIALOG_HEIGHT = 11
DIALOG_WIDTH = 51


def get_dialog_position(dw, dh):
    x = (console.width - dw) // 2
    y = (console.height - dh) // 2
    return (x, y)


class TestApp(App):

    BINDINGS = [("ctrl+d", "show_dialog", "Show Dialog")]

    CSS = """
        Dialog {
            margin-left: %s;
            margin-top: %s;
            layer: dialog;
            width: %s;
            height: %s;
        }
        Screen {
            layers: base dialog;
        }
        #pane1 {
            height: 100%%;
            width: 1fr;
            border-right: solid $secondary-background;
            overflow: hidden;
        }
        #pane2 {
            height: 100%%;
            width: 1fr;
            border-right: solid $secondary-background;
            overflow: hidden;
            background: darkgray;
            color: black;
        }
        #pane3 {
            height: 100%%;
            width: 1fr;
        }
        .hidden {
            display: none;
        }
        #dialog {
            content-align: center middle;
            border: solid brown;
            background: ansi_white;
        }
        #dialog Label {
            text-align: center;
            width: 1fr;
            margin-top: 1;
            color: ansi_red;
        }
    """ % (
        get_dialog_position(DIALOG_WIDTH, DIALOG_HEIGHT) + (DIALOG_WIDTH, DIALOG_HEIGHT)
    )

    def __init__(self):
        super().__init__()
        self.title = "Test App"
        self.dialog_showing = False
        self.dialog = Dialog(classes="hidden")

    def action_show_dialog(self):
        if not self.dialog_showing:
            self.dialog.toggle_class("hidden")
            self.dialog_showing = True

    def hide_dialog(self):
        if self.dialog_showing:
            self.dialog.toggle_class("hidden")
            self.dialog_showing = False

    def on_key(self, event):
        self.hide_dialog()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        pane1 = Vertical(Label("Pane 1"), id="pane1")
        pane2 = Vertical(
            Label("Pane 2"), Label("Press any key to dismiss the dialog"), id="pane2"
        )
        pane3 = Container(Label("Pane 3"), id="pane3")
        yield Horizontal(pane1, pane2, pane3)
        yield self.dialog


app = TestApp()
app.run()
