"""An example of updating a Static with subprocess output.

Don't do this. Ever. This is a bad idea.
"""

import subprocess

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Input, Static

class SubProcessApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Directory to get the `ls` of")
        yield Static(id="ls")

    @on(Input.Submitted)
    def directory_listing(self, event: Input.Submitted) -> None:
        self.query_one("#ls", Static).update(
            subprocess.run(
                f"ls {event.input.value}",
                stdout=subprocess.PIPE,
                shell=True
            ).stdout.decode()
        )

if __name__ == "__main__":
    SubProcessApp().run()

### subprocess_example.py ends here
