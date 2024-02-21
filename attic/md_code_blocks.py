"""https://github.com/Textualize/textual/issues/2400"""

from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Header, Footer, Markdown

MARKDOWN = """\
# Hello world!

Here is some Python code in a code block:

```python
def hello() -> str:
    return "Hello!"
```

Here is some plain text in a code block:

```
Hello!
```

"""


class MDCodeBlocksApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Header()
        with VerticalScroll():
            yield Markdown(MARKDOWN)
        yield Footer()

    def on_mount(self) -> None:
        self.dark = True


if __name__ == "__main__":
    MDCodeBlocksApp().run()
