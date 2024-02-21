from time import sleep
from dataclasses import dataclass

from textual import on, work
from textual.app import App, ComposeResult
from textual.message import Message
from textual.widgets import DataTable, Log
from textual.worker import get_current_worker


class BusyTable(DataTable):

    class Starting(Message):
        pass

    @dataclass
    class Updating(Message):
        on_step: int

    class Finished(Message):
        pass

    def on_mount(self) -> None:
        self.add_columns("Col 1", "Col 2")
        self.load_data()

    @work(thread=True)
    def load_data(self) -> None:
        worker = get_current_worker()
        self.post_message(self.Starting())
        for n in range(100):
            if worker.is_cancelled:
                break
            else:
                sleep(3)
                self.post_message(self.Updating(n))
        self.post_message(self.Finished())

    @on(Updating)
    def update_data(self, event: Updating) -> None:
        self.add_row("New row", str(event.on_step))


class WorkerStateChangeApp(App[None]):

    CSS = """
    Screen > * {
        height: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield BusyTable()
        yield Log()

    @on(BusyTable.Starting)
    @on(BusyTable.Updating)
    @on(BusyTable.Finished)
    def log_message(self, event: Message) -> None:
        self.query_one(Log).write_line(f"{event!r}")


if __name__ == "__main__":
    WorkerStateChangeApp().run()
