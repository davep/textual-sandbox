"""Example for https://github.com/Textualize/textual/issues/3472"""

from time import sleep

from textual import on, work
from textual.app import App, ComposeResult
from textual.widgets import Button, Log
from textual.worker import get_current_worker


class WorkerInWorkerApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Button("Start")
        yield Log()

    @work(thread=True)
    def outer(self) -> None:
        worker = get_current_worker()
        for n in range(50):
            if worker.is_cancelled:
                break
            if n == 10:
                self.call_from_thread(self.inner)
            self.call_from_thread(self.query_one(Log).write_line, f"Outer {n}")
            sleep(0.25)

    @work(thread=True)
    def inner(self) -> None:
        worker = get_current_worker()
        for n in range(50):
            if worker.is_cancelled:
                break
            self.call_from_thread(self.query_one(Log).write_line, f"Inner {n}")
            sleep(0.25)

    @on(Button.Pressed)
    def start(self) -> None:
        self.outer()


if __name__ == "__main__":
    WorkerInWorkerApp().run()
