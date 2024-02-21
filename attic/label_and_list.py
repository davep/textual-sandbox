from textual.app import App, ComposeResult
from textual.containers import Center
from textual.widgets import Label, ListView, ListItem


class LabelAndListViewApp(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }

    ListView {
        width: 30;
        margin: 2 2;
        height: auto;
    }
    """

    def compose(self) -> ComposeResult:
        with Center():
            yield Label("What's the best SciFi show ever?")
        with Center():
            yield ListView(
                ListItem(Label("Firefly?")),
                ListItem(Label("Firefly!")),
                ListItem(Label("Firefly!!")),
                ListItem(Label("Firefly!!!")),
                ListItem(Label("Firefly!!!!")),
            )


if __name__ == "__main__":
    LabelAndListViewApp().run()

### label_and_list.py ends here
