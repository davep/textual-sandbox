from textual.app import App, ComposeResult
from textual.widgets import Static, Footer

class Demo(App):
    TITLE = "Demonstration"
    BINDINGS = [
        ("s", "toggle_sidebar", "Sidebar"),
        ("b", "toggle_bottombar", "Bottombar"),
    ]
    CSS = """
    Screen {
        layout: grid;
        grid-size: 2 5;
    }

    .box {
        height: 100%;
        border: round white;
    }

    #left-main {
        row-span: 5;
    }

    #right-main {
        row-span: 5;
    }

    #sidebar {
        display: none;
        offset-x: -100%;
    }

    Demo.-show-sidebar #sidebar {
        display: block;
        dock: left;

        border: round yellow;

        height: 100%;
        max-width: 33%;
        margin-bottom: 1;

        transition: offset 500ms in_out_cubic;
        offset-x: 0;
    }

    #bottombar {
        display: none;
        offset-y: 100%;
    }

    Demo.-show-bottombar #bottombar {
        display: block;
        dock: bottom;

        border: round red;

        max-height: 33%;
        width: 100%;
        margin-bottom: 1;

        transition: offset 500ms in_out_cubic;
        offset-y: 0;
    }

    Demo.-show-sidebar.-show-bottombar #bottombar {
        offset-x: 47%;
        width: 68%;
    }

    """

    def compose(self) -> ComposeResult:
        # yield Header()
        yield Static(classes="box", id="left-main")
        yield Static(classes="box", id="right-main")
        yield Static(classes="box", id="sidebar")
        yield Static(classes="box", id="bottombar")
        yield Footer()

    def action_toggle_sidebar(self) -> None:
        if "-show-sidebar" in self.classes:
            self.remove_class("-show-sidebar")
        else:
            self.add_class("-show-sidebar")

    def action_toggle_bottombar(self) -> None:
        if "-show-bottombar" in self.classes:
            self.remove_class("-show-bottombar")
        else:
            self.add_class("-show-bottombar")


if __name__ == "__main__":
    Demo().run()

