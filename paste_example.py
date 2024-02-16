"""Example of using the Paste event."""

from textual.app import App
from textual.events import Paste

class PasteExampleApp(App[None]):

    def on_paste(self, event: Paste) -> None:
        self.notify(f"Pasted: {event.text}")

if __name__ == "__main__":
    PasteExampleApp().run()

### paste_example.py ends here
