from textual.app import App, ComposeResult
from textual.widgets import Static
from rich.pretty import Pretty


class Box(Static):

    def compose(self) -> ComposeResult:
        yield Static(classes="style")

    def show_style(self) -> None:
        self.query_one(".style", Static).update(
            Pretty(
                dict(
                    widget=self,
                    background=self.styles.background,
                    border=self.styles.border,
                )
            )
        )


class BorderTest(App[None]):

    CSS = """
    Screen {
        layout: grid;
        grid-size: 3 2;
    }

    Static {
        height: 100%;
    }

    #css-border-no-background {
        border: solid red;
        background: #fff0;
    }

    #css-border-and-background {
        border: solid red;
        background: #000;
    }

    #css-no-border-background {
        background: #000;
    }
    """

    def compose(self) -> ComposeResult:
        yield Box(id="css-border-no-background")
        yield Box(id="css-no-border-background")
        yield Box(id="css-border-and-background")
        yield Box(id="code-border-no-background")
        yield Box(id="code-no-border-background")
        yield Box(id="code-border-and-background")

    def on_mount(self) -> None:
        self.query_one("#code-border-no-background", Box).styles.border = (
            "solid",
            "red",
        )
        self.query_one("#code-no-border-background", Box).styles.background = "#000"
        self.query_one("#code-border-and-background", Box).styles.border = (
            "solid",
            "red",
        )
        self.query_one("#code-border-and-background", Box).styles.background = "#000"
        for box in self.query(Box):
            box.show_style()


if __name__ == "__main__":
    BorderTest().run()
