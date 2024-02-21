"""Example of different worker steps.

For a question on Discord.
"""

from time import sleep

from textual import on, work
from textual.app import App, ComposeResult
from textual.message import Message
from textual.widgets import Button, Log


class WorkerStepsApp(App[None]):

    class Step1Complete(Message):
        pass

    class Step2Complete(Message):
        pass

    def compose(self) -> ComposeResult:
        yield Button("GO!")
        yield Log()

    @on(Button.Pressed)
    def start_steps(self) -> None:
        self.query_one(Button).disabled = True
        self.step1()

    @on(Step1Complete)
    def start_step2(self) -> None:
        self.query_one(Log).write_line("=== Did that, now for the next bit ===")
        self.step2()

    @on(Step2Complete)
    def all_done(self) -> None:
        self.query_one(Button).disabled = False
        self.notify("Hey! Look! We're all done!")

    @work(thread=True)
    def step1(self) -> None:
        log = self.query_one(Log)
        for n in range(10):
            self.call_from_thread(log.write_line, f"Step 1 part {n}")
            sleep(0.5)
        self.post_message(self.Step1Complete())

    @work(thread=True)
    def step2(self) -> None:
        log = self.query_one(Log)
        for n in range(10):
            self.call_from_thread(log.write_line, f"Step 2 part {n}")
            sleep(0.5)
        self.post_message(self.Step2Complete())


if __name__ == "__main__":
    WorkerStepsApp().run()

### worker_steps.py ends here
