"""https://github.com/Textualize/textual/issues/4455"""

from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Markdown

MARKDOWN = """

## Have some code:

```lisp
(defconstant +byte+ '(unsigned-byte 8)
  "Type of a byte array element.")

(defconstant +2bit-version+ 0
  "The only valid version number of 2bit data.")

(defconstant +signature+ #x1a412743
  "2bit file signature.")

(defconstant +bases+ #("T" "C" "A" "G")
  "Vector of the bases.

Note that the positions of each base in the vector map to the 2bit decoding
for them.")
```

## Now a list:

- This
- Is
- A
- List
- Really
"""


class ScrollEndWithMarkdownApp(App[None]):
    CSS = """
    Label {
        padding: 3 0;
    }
    """

    def compose(self) -> ComposeResult:
        yield VerticalScroll()

    async def on_mount(self) -> None:
        await self.query_one(VerticalScroll).mount_all(
            [Markdown(f"# This is Markdown {n}{MARKDOWN}") for n in range(50)]
        )
        self.query_one(VerticalScroll).scroll_end(animate=False)


if __name__ == "__main__":
    ScrollEndWithMarkdownApp().run()

### scroll_end.py ends here
