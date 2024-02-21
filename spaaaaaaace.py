"""For a question about binding space, on Discord."""

from textual.app import App, ComposeResult
from textual.widgets import Tree, Static, Footer


class SpaceWidget(Static, can_focus=True):

    DEFAULT_CSS = """
    SpaceWidget {
        border: none;
        background: cornflowerblue 50%;
        width: 1fr;
        height: 1fr;
    }

    SpaceWidget:focus {
        border: cornflowerblue double 50%;
        background: cornflowerblue;
    }
    """

    BINDINGS = [
        ("space", "space", "Don't press space!!!"),
    ]

    def action_space(self) -> None:
        self.notify("Spaaaaaaaaaaaaaaaace!")


class SpaaaaaaaaaaaaceApp(App[None]):

    CSS = """
    Screen {
        layout: horizontal;
    }
    """

    def compose(self) -> ComposeResult:
        yield Tree("Root")
        yield SpaceWidget()
        yield Footer()

    def on_mount(self) -> None:
        personality = self.query_one(Tree).root.add("Personality")
        personality.add_leaf("Central")
        personality.add_leaf("Morality")
        personality.add_leaf("Curiosity")
        personality.add_leaf("Intelligence")
        personality.add_leaf("Anger")
        personality.add_leaf("Intelligence")
        corrupted = self.query_one(Tree).root.add("Corrupted")
        corrupted.add_leaf("Space")
        corrupted.add_leaf("Adventure")
        corrupted.add_leaf("Fact")


if __name__ == "__main__":
    SpaaaaaaaaaaaaceApp().run()

### spaaaaaaace.py ends here
