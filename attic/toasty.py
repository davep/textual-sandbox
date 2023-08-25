from __future__ import annotations

from pathlib import Path
from random import choice
from subprocess import run

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import Markdown, Button, Checkbox, Input
from textual.notifications import SeverityLevel, Notification

QUOTES = [
    "Are either of you paleontologists? I'm in desperate need of a paleontologist.",
    "I should reach Defcon 1 and release my missiles in 28 hours. Would you like to see some projected kill ratios?",
    "A strange game."
    "The only winning move is not to play.",
    "How about a nice game of chess?",
    "Joshua called me.",
    "The WOPR spends all it's time thinking about World War III.",
    "Did you ever play tic-tac-toe?",
    "I loved it when you nuked Las Vegas."
]

class ToastyApp(App[None]):

    CSS = """
    Horizontal {
        align: center middle;
        height: auto;
    }
    Horizontal Button {
        margin-left: 1;
    }
    Input {
        width: 20%;
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical():
            with Horizontal():
                yield Checkbox("Titled", value=True)
                yield Input(placeholder="Timeout (default 3 seconds)")
                yield Button("Information", id="information")
                yield Button("Warning", id="warning")
                yield Button("Error", id="error")
            with VerticalScroll():
                yield Markdown()

    async def on_mount(self) -> None:
        await self.query_one(Markdown).load(Path("/Users/davep/develop/python/textual/README.md"))

    def _refresh_notifications(self) -> None:
        for notification in self._notifications:
            title = notification.severity.capitalize() if notification.title is None else notification.title
            run([
                "osascript",
                "-e",
                f'display notification \"{notification.message}\" with title \"{title}\"'
            ])
        self._notifications.clear()

    @on(Button.Pressed)
    def yell(self, event: Button.Pressed) -> None:
        try:
            timeout = float(self.query_one(Input).value)
        except ValueError:
            timeout = 3
        self.notify(
            choice(QUOTES),
            severity=event.button.id,
            title=None if self.query_one(Checkbox).value else "",
            timeout=timeout
        )

if __name__ == "__main__":
    ToastyApp().run()
