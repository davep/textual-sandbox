"""https://github.com/Textualize/textual/issues/4088"""

from textual.app import App
from textual.widgets import TabbedContent, TabPane


class AwaitableTypeWarningApp(App[None]):

    async def on_mount(self) -> None:
        await self.query_one(TabbedContent).add_pane(TabPane("Test"))
        await self.query_one(TabbedContent).remove_pane("some-tab")


### await_type_warning.py ends here
