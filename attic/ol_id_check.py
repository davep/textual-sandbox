from textual import on
from textual.app import App, ComposeResult
from textual.widgets import OptionList, TextLog
from textual.widgets.option_list import Option

class OptionListIDTestApp(App[None]):

    def compose(self) -> ComposeResult:
        yield OptionList(
            *[Option(f"Via compose {n}", id=f"compose-{n}") for n in range(5)]
        )
        yield TextLog()

    def on_mount(self) -> None:
        self.query_one(OptionList).add_option(
            Option("Via add_option", id="add_option")
        )
        self.query_one(OptionList).add_options(
            [Option(f"Via add_options {n}", id=f"add-options-{n}") for n in range(5)]
        )

    @on(OptionList.OptionMessage)
    def log_message(self, event: OptionList.OptionMessage) -> None:
        self.query_one(TextLog).write(f"{event.__class__.__name__} {event.option.id=}")

if __name__ == "__main__":
    OptionListIDTestApp().run()
