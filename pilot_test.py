"""https://discord.com/channels/1026214085173461072/1033754296224841768/1164281860445179924"""

from asyncio import run

from textual.app import App, ComposeResult
from textual.widgets import Input

class PilotClickTestApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Input(id="not-me")
        yield Input(id="me")

async def test_pilot_click() -> None:
    async with PilotClickTestApp().run_test() as pilot:
        await pilot.click("#me")
        assert pilot.app.screen.focused is not None
        assert pilot.app.screen.focused.id == "me"
        await pilot.press("1", "full_stop", "4", "1", "4", "6")
        assert pilot.app.query_one("#me", Input).value == "1.4146"

if __name__ == "__main__":
    run(test_pilot_click())

### pilot_test.py ends here
