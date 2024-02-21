from time import sleep

from textual import on, work
from textual.app import App, ComposeResult
from textual.widgets import Button, ProgressBar
from textual.worker import get_current_worker


class WorkWithProgress(App[None]):

    def compose(self) -> ComposeResult:
        yield Button("Press me to do some work")
        yield ProgressBar(total=50)

    @on(Button.Pressed)
    def start_some_work(self) -> None:
        self.do_something_for_a_while()

    # We're going to do this in a threaded worker, because then it can run
    # in a "normal" loop while also allowing Textual to carry on doing its
    # thing.
    @work(thread=True, exclusive=True)
    def do_something_for_a_while(self) -> None:
        # We grab a reference to the worker because we will be checking if
        # it's been cancelled.
        worker = get_current_worker()
        # Grab a reference to the progress bar so it's easier to work with.
        progress = self.query_one(ProgressBar)
        # Set the initial conditions for the progress brar.
        self.call_from_thread(progress.update, progress=0)
        # For the number of steps mentioned...
        for _ in range(50):
            # ...sleep for a second, as a stand-in for some of work.
            sleep(1)
            # Check if we've been cancelled. If we have stop working.
            if worker.is_cancelled:
                break
            # Advance the progress bar. Note the use of `call_from_thread`.
            # We could also use a custom message here too.
            # https://textual.textualize.io/guide/workers/#posting-messages
            self.call_from_thread(progress.advance)


if __name__ == "__main__":
    WorkWithProgress().run()

### work_with_progress.py ends here
