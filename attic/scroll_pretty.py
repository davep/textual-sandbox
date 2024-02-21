from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Pretty


class ScrollPrettyApp(App[None]):

    def compose(self) -> ComposeResult:
        with VerticalScroll():
            yield Pretty(
                [
                    f"All work and no play makes Jack a dull boy - {n}"
                    for n in range(1000)
                ]
            )


if __name__ == "__main__":
    ScrollPrettyApp().run()
