"""Testing spacing in a Markdown document."""

from textual.app import App, ComposeResult
from textual.widgets import Markdown

EXAMPLE_MARKDOWN = """\
Multiple white spaces   _are_   flattened.

[No    extra     spaces      here              ](http://example.com).

_Definitely     no extra     spaces          here_.

Tabs before here		More tabs

**No   bold   ones either              TOO**.

In here `the   space      must            flow`!.

```python
class     Foo(    Object ):
    pass
```

"""


class MarkdownExampleApp(App):
    def compose(self) -> ComposeResult:
        yield Markdown(EXAMPLE_MARKDOWN)


if __name__ == "__main__":
    MarkdownExampleApp().run()

### markdown_spacing.py ends here
