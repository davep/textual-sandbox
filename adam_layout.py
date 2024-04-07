"""Example layout for a question on Discord."""

from textual.app import App, ComposeResult
from textual.containers import Center, Horizontal, Vertical, VerticalScroll
from textual.widgets import Label, Switch


class AdamLayoutApp(App[None]):
    CSS = """
    Screen {
        align: center middle;
    }

    .home {
        border: panel cornflowerblue;
        width: 80%;
        height: 80%;
        align: center middle;
    }

    .switches {
        width: 50%;
        height: 50%;
    }

    .switcher {
        background: $primary;
        margin: 0 1 1 1;
        padding: 0 0 0 1;
        height: auto;

        Label {
            height: 100%;
            content-align: left middle;
            width: 1fr;
        }

        &.last {
            margin: 0 1 0 1;
        }
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical(classes="home") as home, VerticalScroll(classes="switches"):
            home.border_title = "Home"
            last_switch: Horizontal | None = None
            for _ in range(30):
                with Center(), Horizontal(classes="switcher") as last_switch:
                    yield Label("Text")
                    yield Switch()
            if last_switch is not None:
                last_switch.add_class("last")


if __name__ == "__main__":
    AdamLayoutApp().run()

### adam_layout.py ends here
