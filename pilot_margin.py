"""Example for https://github.com/Textualize/textual/issues/4412"""

from asyncio import run

from textual.app import App, ComposeResult
from textual.widget import Widget


class PilotMarginApp(App[None]):
    CSS = """
    #click-me {
        margin: 200;
        width: 20;
        height: 10;
        border: solid red;
        background: green;
    }
    """

    def compose(self) -> ComposeResult:
        yield Widget(id="click-me")


async def test_app():
    async with PilotMarginApp().run_test(size=(400, 400)) as pilot:
        await pilot.click("#click-me")


if __name__ == "__main__":
    run(test_app())

### pilot_margin.py ends here
