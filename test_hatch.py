"""Illustrate https://github.com/Textualize/textual/issues/4605"""

from textual.app import App


class HatchApp(App[None]):
    CSS = """
    Screen {
        hatch: cross red;
    }
    """


if __name__ == "__main__":
    HatchApp().run()

### test_hatch.py ends here
