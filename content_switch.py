"""Add an example of adding more stuff to a ContentSwitcher."""

from textual.app import App, ComposeResult
from textual.reactive import var
from textual.widgets import ContentSwitcher, Label


class ContentSwitchApp(App[None]):
    BINDINGS = [
        ("space", "more"),
    ]

    count: var[int] = var(0)

    def compose(self) -> ComposeResult:
        yield ContentSwitcher()

    def action_more(self) -> None:
        self.query_one(ContentSwitcher).mount(
            Label(f"Label {self.count}", id=f"content-{self.count}")
        )
        self.query_one(ContentSwitcher).current = f"content-{self.count}"
        self.count += 1


if __name__ == "__main__":
    ContentSwitchApp().run()

### content_switch.py ends here
