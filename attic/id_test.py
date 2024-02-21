from textual.app import App
from textual.widgets import Static


class IDTest(App[int]):

    BINDINGS = [("q", "return", "Return the result")]

    def compose(self):
        for _ in range(30):
            yield Static("The only good bug is a dead bug!", id="quote")

    def action_return(self):
        self.exit(len(self.query("#quote")))


if __name__ == "__main__":
    print(f"I found this many quotes: {IDTest().run()}")
