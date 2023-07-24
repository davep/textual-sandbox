"""https://github.com/Textualize/textual/issues/2958"""

from __future__ import annotations
from rich.console import RenderableType
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, ScrollableContainer
from textual.widgets import Button, Footer, Header, Select, Static, TextLog, Placeholder, Markdown

__ISSUE_MD__ = """
## Question #1 -- How do I make selecting the option list _NOT_ scroll the parent container
This issue is that even when the Select widget has space on screen to display, it still scrolls which mis-aligns
the parent container on the screen.

I am trying to find a way to keep the section aligned while still having the drop-down expand if needed
to a certain degree, maybe _X_ items long or a max-height value

## Question #2 - What's the best way for the Select widget to _lose_ focus when the user clicks elsewhere?
Example:
    If you open the dropdown then click a quick-access link on the left the dropdown menu doesn't naturally close

What's the ideal way to close the list when _anything_ else is clicked?
(I am assuming by overriding the on_click function and checking for focus somehow)

"""

WELCOME_MD = """
## Textual Layout Issue / Question
**Hello**! Textual is amazing and I'm having so much fun learning it!
There are _so_ _many_ potential projects I can use it for!
"""

WIDGETS_MD = """
Textual widgets are _amazingly_ powerful interactive components.
I've been working on building my own -> That's where I found this and couldn't figure it
out
"""


class Welcome(Container):
    def compose(self) -> ComposeResult:
        yield Markdown(WELCOME_MD)
        yield Button("Start", variant="success")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.add_note("[b magenta]Start!")
        self.app.query_one(".location-first").scroll_visible(duration=0.5, top=True)


class Title(Static):
    pass


class Body(ScrollableContainer):
    pass


class QuickAccess(Container):
    pass


class AboveFold(Container):
    pass


class Section(Container):
    pass


class SectionTitle(Static):
    pass


class Column(Container):
    pass


class TextContent(Static):
    pass


class LocationLink(Static):
    def __init__(self, label: str, reveal: str) -> None:
        super().__init__(label)
        self.reveal = reveal

    def on_click(self) -> None:
        self.app.set_focus(None)
        self.app.query_one(self.reveal).scroll_visible(top=True, duration=0.5)
        self.app.add_note(f"Scrolling to [b]{self.reveal}[/b]")


class DemoApp(App[None]):
    CSS_PATH = "select_focus_oddness.css"
    TITLE = "Question - Is this a bug?"
    BINDINGS = [
        ("f1", "app.toggle_class('TextLog', '-hidden')", "Notes"),
        Binding("ctrl+c,ctrl+q", "app.quit", "Quit", show=True),
    ]

    # Overloaded the __init__ section so that we could enable watching the CSS file
    def __init__(self):
        super().__init__(watch_css=True)

    # I lef the note section in for debugging, but wasn't sure what exactly to log while modifying the CSS
    def add_note(self, renderable: RenderableType) -> None:
        self.query_one(TextLog).write(renderable)

    def compose(self) -> ComposeResult:
        yield Container(
            Header(show_clock=False),
            TextLog(classes="-hidden", wrap=False, highlight=True, markup=True),
            Body(
                QuickAccess(
                    LocationLink("Home", ".location-top"),
                    LocationLink("Bugged Section", ".location-widgets"),
                ),
                AboveFold(Welcome(), classes="location-top"),
                Column(
                    Section(
                        SectionTitle("Example Section Title"),
                        Markdown(WIDGETS_MD),
                        Placeholder("-- Example space of n+ other widgets and their children --"),
                        Select([("Example Selectable Option", 1)],
                               prompt="Please choose an option.. (And watch it scroll)"),
                        Markdown(__ISSUE_MD__, id="issue-markdown"),
                        id="bugged-section"
                    ),
                    classes="location-widgets location-first",
                )
            )
        )
        yield Footer()

    def on_mount(self) -> None:
        self.add_note("?? Question ?? is running")
        self.query_one("Welcome Button", Button).focus()


app = DemoApp()
if __name__ == "__main__":
    app.run()
