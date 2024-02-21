from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import ContentSwitcher, Input


class ContentSwitcherFocusApp(App[None]):

    CSS = """
    ContentSwitcher {
        border: solid red;
    }
    """

    BINDINGS = [
        ("f1", "go(0)"),
        ("f2", "go(1)"),
        ("f3", "go(2)"),
        ("f4", "go(3)"),
        ("f5", "go(4)"),
    ]

    def compose(self) -> ComposeResult:
        with ContentSwitcher(initial="content-0"):
            for n in range(10):
                with Vertical(id=f"content-{n}"):
                    yield Input(placeholder=f"{n}")

    def action_go(self, content: int) -> None:
        self.query_one(ContentSwitcher).current = f"content-{content}"
        self.query(f"#content-{content} > *").first().focus()


if __name__ == "__main__":
    ContentSwitcherFocusApp().run()
