"""https://github.com/Textualize/textual/discussions/3026"""

from dataclasses import dataclass

from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.message import Message
from textual.widgets import TabbedContent, TabPane, Button, Footer, Label


class BasePane(TabPane):

    BINDINGS = [
        Binding("f1", "invoke('the_f1_action')", "First thing"),
        Binding("f2", "invoke('the_f2_action')", "Second thing"),
    ]

    @dataclass
    class TabPaneAction(Message):
        action: str

    def action_invoke(self, action: str) -> None:
        self.post_message(self.TabPaneAction(action))


class FirstPane(BasePane):

    def compose(self) -> ComposeResult:
        yield Button("This is the first pane")


class SecondPane(BasePane):

    BINDINGS = [
        Binding("f3", "invoke('one_more_thing')", "Also this too"),
        Binding("f4", "invoke('even_more')", "Yes more"),
        Binding("f5", "invoke('that_is_enough')", "No more bindings please"),
    ]

    def compose(self) -> ComposeResult:
        yield Button("This is the second pane")


class TabbedContentBindings(App[None]):

    def compose(self) -> ComposeResult:
        yield Label("The pressed binding will appear here")
        with TabbedContent():
            yield FirstPane("First")
            yield SecondPane("Second")
        yield Footer()

    @on(BasePane.TabPaneAction)
    def perform_action(self, event: BasePane.TabPaneAction) -> None:
        # Here we'd treat event.action as some sort of ID to work off.
        self.query_one(Label).update(f"We've been asked to run a {event.action}")


if __name__ == "__main__":
    TabbedContentBindings().run()
