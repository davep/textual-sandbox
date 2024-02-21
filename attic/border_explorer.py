from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Header, Footer, Static


class BorderExplorerApp(App[None]):

    CSS = """
    Grid {
        width: 1fr;
        height: 1fr;
        grid-size: 4;
    }

    Static {
        background: $panel;
        width: 100%;
        height: 100%;
    }

    #border-0  { border: solid; }
    #border-1  { border: solid red; }
    #border-2  { border: solid red green; }
    #border-3  { border: solid red green blue; }
    #border-4  { border: solid red green blue yellow; }
    #border-5  { border: solid red green blue yellow white; }
    #border-6  { border: solid dashed; }
    #border-7  { border: solid dashed round; }
    #border-8  { border: solid dashed round yellow; }
    #border-9  { border: solid dashed round yellow outer; }
    #border-10 { border: solid dashed round yellow outer ascii; }
    #border-11 { border: solid dashed round yellow outer ascii green; }
    #border-12 { border: solid solid green green red red brown solid orange; }
    #border-13 { border: solid solid solid solid solid solid solid solid solid solid solid solid solid solid; }
    #border-14 { border: orange orange orange orange orange orange orange orange orange orange orange orange orange ; }
    #border-15 { border: none none none none none none none none none none none none none none none none none none none solid; }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Grid():
            for n in range(4 * 4):
                yield Static(f"Border {n}", id=f"border-{n}")
        yield Footer()


if __name__ == "__main__":
    BorderExplorerApp().run()
