"""https://github.com/Textualize/textual/issues/4248"""

from textual.app import App, ComposeResult
from textual.widgets import Label


class ClickMRE(App):
    def compose(self) -> ComposeResult:
        yield Label(
            "[@click]click me and crash[/]"
        )  # ValueError in run_action on click
        yield Label(
            "[@click=]click me and crash[/]"
        )  # ValueError in run_action on click
        yield Label(
            "[@click=()]click me and crash[/]"
        )  # ValueError in run_action on click
        yield Label("[@click=foobar]click me[/]")  # ok, nothing happens
        yield Label("[@click=foobar()]click me[/]")  # ok, nothing happens
        yield Label("[@click=toggle_dark]click me[/]")  # ok, works fine
        yield Label("[@click=toggle_dark()]click me[/]")  # ok, works fine


if __name__ == "__main__":
    ClickMRE().run()

### click_markup.py ends here
