"""https://github.com/Textualize/textual/discussions/3167"""

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import OptionList, Label, Input, ContentSwitcher
from textual.widgets.option_list import Option

class ContentSwitchApp(App[None]):

    CSS = """
    OptionList {
        width: 1fr;
    }

    OptionList:focus {
        border: blank;
    }

    ContentSwitcher {
        width: 4fr;
    }

    Label {
        padding-left: 1;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield OptionList(
                Option("First", "nav-1"),
                Option("Second", "nav-2"),
                Option("Third", "nav-3"),
            )
            with ContentSwitcher(initial="nav-1"):
                with Vertical(id="nav-1"):
                    yield Label("Some input:")
                    yield Input()
                    yield Label("Some other input:")
                    yield Input()
                with Vertical(id="nav-2"):
                    yield Label("A second set of some input:")
                    yield Input()
                    yield Label("A second set of some other input:")
                    yield Input()
                with Vertical(id="nav-3"):
                    yield Label("Hey look a third set of some input:")
                    yield Input()
                    yield Label("Hey look a third set of some other input:")
                    yield Input()

    @on(OptionList.OptionSelected)
    def switch(self, event: OptionList.OptionSelected) -> None:
        self.query_one(ContentSwitcher).current = event.option_id

if __name__ == "__main__":
    ContentSwitchApp().run()

### vertical_content_switch.py ends here
