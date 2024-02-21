"""https://github.com/Textualize/textual/issues/1608"""

from asyncio import run
from textual.app import App
from textual.screen import Screen
from textual.widget import Widget


class MyWidget(Widget):
    def compose(self):
        yield Widget()


class MyScreen(Screen):

    def compose(self):
        yield MyWidget()


class MyApp(App):

    def on_mount(self):
        self.install_screen(MyScreen(), "myscreen")
        self.push_screen("myscreen")


async def test_this():
    app = MyApp()
    async with app.run_test():
        raise Exception("never raised")
        assert True


run(test_this())
