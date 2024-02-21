from textual import work

"""https://github.com/Textualize/textual/discussions/3265"""

from textual.worker import get_current_worker
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class DuplicateIDError_App(App):
    """Too many toasts too fast produces duplicate widget ID error"""

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()

    @work(exclusive=False, thread=True)
    async def func1(self) -> None:
        worker = get_current_worker()
        if not worker.is_cancelled:
            self.call_from_thread(self.notify, "func1!")

    @work(exclusive=False, thread=True)
    async def func2(self) -> None:
        worker = get_current_worker()
        if not worker.is_cancelled:
            self.call_from_thread(self.notify, "func2")

    @work(exclusive=False, thread=True)
    async def func3(self) -> None:
        worker = get_current_worker()
        if not worker.is_cancelled:
            self.call_from_thread(self.notify, "func3")

    @work(exclusive=False, thread=True)
    async def func4(self) -> None:
        worker = get_current_worker()
        if not worker.is_cancelled:
            self.call_from_thread(self.notify, "func4")

    def timers_mount(self, _timers: dict):
        for k in _timers:

            _interval = int(_timers[k])
            _func_str = "self.app." + k

            self.set_interval(_interval, eval(_func_str))

    def on_mount(self):
        func_names_and_intervals = {"func1": 5, "func2": 10, "func3": 2, "func4": 4}
        self.timers_mount(func_names_and_intervals)


if __name__ == "__main__":

    app = DuplicateIDError_App()
    app.title = "Duplicate ID Error Demo"
    app.run()
