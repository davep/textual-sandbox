from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Label


class TabColourApp(App[None]):

    CSS = """
    .red {
        color: red;
    }
    .green {
        color: green;
    }
    .blue {
        color: blue;
    }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent():
            for n in range(10):
                with TabPane(f"Tab {n}", id=f"tab-{n}"):
                    yield Label(f"This is tab {n}")

    def on_mount(self) -> None:
        self.query_one("Tab#tab-3").set_classes("green")


if __name__ == "__main__":
    TabColourApp().run()
