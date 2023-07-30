from textual.app        import App, ComposeResult
from textual.containers import Container
from textual.widgets    import TabbedContent, TabPane, Label

class DocksInTabPanesApp( App[ None ] ):

    CSS = """
    TabbedContent ContentSwitcher {
        height: 1fr;
    }

    TabPane {
        height: 100%;
    }

    #top {
        dock: top;
        height: 4;
        background: red;
    }

    #left {
        dock: left;
        width: 8;
        background: green;
    }

    #bottom {
        dock: bottom;
        height: 4;
        background: blue;
    }

    #right {
        dock: right;
        width: 8;
        background: orange;
    }
    """

    def compose( self ) -> ComposeResult:
        with TabbedContent():
            for where in ("top", "left", "bottom", "right"):
                with TabPane(where.capitalize()):
                    with Container(id=where):
                        yield Label(where)


if __name__ == "__main__":
    DocksInTabPanesApp().run()
