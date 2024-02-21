"""https://github.com/Textualize/textual/discussions/3968"""

from textual.app import App, ComposeResult
from textual.widgets import Label, Input


class RemountApp(App[None]):

    BINDINGS = [("f1", "sync"), ("f2", "async")]

    def compose(self) -> ComposeResult:
        for n in range(1_000):
            yield Label(f"This is label {n}")
            yield Input(placeholder=f"This is input {n}")

    def action_sync(self) -> None:
        with self.batch_update():
            self.query("Label, Input").remove()
            self.mount_all(self.compose())

    async def action_async(self) -> None:
        with self.batch_update():
            await self.query("Label, Input").remove()
            await self.mount_all(self.compose())


if __name__ == "__main__":
    RemountApp().run()

### remount.py ends here
