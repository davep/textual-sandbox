"""Example of just running code, no interaction."""

from time import sleep

from textual import work
from textual.app import App, ComposeResult
from textual.widgets import Log
from textual.worker import get_current_worker

class JustRunNoInteractAp(App[None]):

    def compose(self) -> ComposeResult:
        yield Log()

    @work(thread=True)
    def do_stuff(self) -> None:
        worker = get_current_worker()
        log = self.query_one(Log)
        n = 0
        while not worker.is_cancelled:
            self.call_from_thread(log.write_line, str(n))
            sleep(0.5)
            n += 1

    def on_mount(self) -> None:
        self.do_stuff()

if __name__ == "__main__":
    JustRunNoInteractAp().run()

### just_run.py ends here
