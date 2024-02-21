from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import Label


class OptionalCSSApp(App[None]):

    BINDINGS = [
        ("r", "refresh"),
    ]

    def compose(self) -> ComposeResult:
        yield Label("This should be optionally changeable.")

    def load_css_from(self, css_file: Path) -> None:
        if css_file.exists():
            new_style_sheet = self.stylesheet.copy()
            new_style_sheet.read_all([css_file])
            new_style_sheet.parse()
            self.stylesheet = new_style_sheet
            self.stylesheet.update(self)
            self.screen.refresh(layout=True)

    def action_refresh(self) -> None:
        self.load_css_from(Path("option_css.css"))


if __name__ == "__main__":
    OptionalCSSApp().run()
