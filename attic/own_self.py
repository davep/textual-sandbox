"""Bad ID tester.

https://github.com/Textualize/textual/issues/659
"""

from textual.app import App
from textual.widget import Widget


class SelfOwn(Widget):

    def __init__(self) -> None:
        super().__init__(self)


class SelfOwnage(App[None]):

    def compose(self):
        yield SelfOwn()


if __name__ == "__main__":
    SelfOwnage().run()
