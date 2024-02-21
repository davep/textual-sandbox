from textual import on
from textual.app import App, ComposeResult
from textual.reactive import var
from textual.widgets import Button, Label


class QueryAfterMountExample(App[None]):

    counter: var[int] = var(0)

    def compose(self) -> ComposeResult:
        yield Button("Test")

    @on(Button.Pressed)
    async def test(self) -> None:
        next_id = f"test-{self.counter}"
        await self.screen.mount(Label(next_id, id=next_id))
        self.notify(f"{self.query_one(f'#{next_id}')}")
        self.counter += 1


if __name__ == "__main__":
    QueryAfterMountExample().run()

### query_after_mount.py ends here
