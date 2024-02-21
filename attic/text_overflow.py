from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Static
from rich.text import Text


class Box(Container):

    DEFAULT_CSS = "Box { border: solid red; height: auto; background: #555; }"

    def compose(self) -> ComposeResult:
        yield Static(
            Text(
                "Happiness, free, for everyone, and let no one be forgotten!",
                no_wrap=True,
                overflow="ellipsis",
            )
        )


class OverflowApp(App[None]):

    def compose(self) -> ComposeResult:
        for n in range(16):
            yield (box := Box())
            box.styles.width = (1 + n) * 4


if __name__ == "__main__":
    OverflowApp().run()
