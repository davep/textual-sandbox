from asyncio import sleep

from textual import on, work
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.reactive import var
from textual.widgets import Button, Log


class WaitForWorkersApp(App[None]):

    shutting_down: var[bool] = var(False)

    def compose(self) -> ComposeResult:
        yield Button("Cancel workers")
        with Horizontal():
            for n in range(5):
                yield Log(id=f"log{n}")
            yield Log(id="status")

    @work(group="busy-work")
    async def make_busy(self, work_id: int) -> None:
        n = 0
        while not self.shutting_down:
            await sleep(5 / (work_id + 1))
            self.query_one(f"#log{work_id}", Log).write_line(f"Ping {n}")
            n += 1
        self.query_one(f"#log{work_id}", Log).write_line("I'm done")

    def on_mount(self) -> None:
        for n in range(5):
            self.make_busy(n)

    @on(Button.Pressed)
    def start_closedown(self) -> None:
        self.closedown()

    @work
    async def closedown(self) -> None:
        self.query_one("#status", Log).write_line("Starting shutdown")
        self.shutting_down = True
        await self.workers.wait_for_complete(
            [worker for worker in self.workers if worker.group == "busy-work"]
        )
        self.query_one("#status", Log).write_line("All workers finished, I'd quit here")


if __name__ == "__main__":
    WaitForWorkersApp().run()

### wait_for_workers.py ends here
