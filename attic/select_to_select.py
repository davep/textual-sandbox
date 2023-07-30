"""https://github.com/Textualize/textual/discussions/2840"""

from __future__ import annotations

from dataclasses import dataclass

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Select
from textual.widget import Widget
from textual.message import Message
from textual.reactive import var

CAMPAIGNS = [
    ("One", "1"),
    ("Two", "2"),
    ("Three", "3"),
]

SCENARIOS = {
    "1": [
        ("Foo", "1.1"),
        ("Bar", "1.2"),
        ("Baz", "1.3"),
    ],
    "2": [
        ("Wibble", "2.1"),
        ("Wobble", "2.2"),
        ("Wubble", "2.3"),
    ],
    "3": [
        ("One", "3.1"),
        ("More", "3.2"),
        ("Example", "3.3"),
    ],
}

class Campaign(Widget):

    @dataclass
    class Selected(Message):
        campaign: Campaign
        selected: str

        @property
        def control(self) -> Campaign:
            return self.campaign

    def compose(self) -> ComposeResult:
        yield Select(CAMPAIGNS, prompt="Select a campaign")

    @on(Select.Changed)
    def new_campaign(self, event: Select.Changed) -> None:
        if event.select.value is not None:
            self.post_message(self.Selected(self, event.select.value))

class Scenario(Widget):

    campaign: var[str] = var[str]("")

    def compose(self) -> ComposeResult:
        yield Select([], prompt="Scenario")

    def watch_campaign(self) -> None:
        if self.campaign:
            self.query_one(Select).set_options(SCENARIOS[self.campaign])

class SelectToSelectApp(App[None]):

    CSS = """
    Campaign, Scenario {
        width: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Campaign()
            yield Scenario()

    @on(Campaign.Selected)
    def switch_campaign(self, event: Campaign.Selected) -> None:
        self.query_one(Scenario).campaign = event.selected

if __name__ == "__main__":
    SelectToSelectApp().run()
