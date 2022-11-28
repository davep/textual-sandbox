from textual.app import App, ComposeResult
from textual.widgets import Static

class Greetings(App[None]):

    def __init__(self, greeting: str="Hello", to_greet: str="World") -> None:
        self.greeting = greeting
        self.to_greet = to_greet
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Static(f"{self.greeting}, {self.to_greet}")

if __name__=="__main__":
    Greetings().run()
    Greetings(to_greet="davep").run()
    Greetings("Well hello", "there").run()
