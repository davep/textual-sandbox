"""https://github.com/Textualize/textual/issues/3095"""

from textual.app import App

class GNDN(App[None]):

    def on_ready(self) -> None:
        self.exit()

if __name__ == "__main__":
    GNDN().run()

### gndn.py ends here
