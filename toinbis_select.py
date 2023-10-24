from textual.app import App, ComposeResult
from textual.widgets import Select

class DemoApp(App[None]):

    DEFAULT_CSS = """
    #selector {
        width: 20%;
    }

    #selector:focus > SelectCurrent {
        border: tall green;
    }

    #selector.-expanded > SelectCurrent {
        border: tall green;
    }
    """

    def compose(self) -> ComposeResult:
        yield Select([("First", 1), ("Second", 2)], id="selector")

if __name__ == "__main__":
    DemoApp().run()

### toinbis_select.py ends here
