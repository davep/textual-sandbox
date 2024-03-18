"""Tester code for the new soft-wrap in TextArea."""

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import TextArea

INITIAL = """\
No one would have believed in the last years of the nineteenth century that this world was being watched keenly and closely by intelligences greater than man's and yet as mortal as his own; that as men busied themselves about their various concerns they were scrutinised and studied, perhaps almost as narrowly as a man with a microscope might scrutinise the transient creatures that swarm and multiply in a drop of water. With infinite complacency men went to and fro over this globe about their little affairs, serene in their assurance of their empire over matter. It is possible that the infusoria under the microscope do the same. No one gave a thought to the older worlds of space as sources of human danger, or thought of them only to dismiss the idea of life upon them as impossible or improbable. It is curious to recall some of the mental habits of those departed days. At most terrestrial men fancied there might be other men upon Mars, perhaps inferior to themselves and ready to welcome a missionary enterprise. Yet across the gulf of space, minds that are to our minds as ours are to those of the beasts that perish, intellects vast and cool and unsympathetic, regarded this earth with envious eyes, and slowly and surely drew their plans against us. And early in the twentieth century came the great disillusionment.

"""


class TexMacs(TextArea):
    def __init__(self, soft_wrap: bool, id: str) -> None:
        super().__init__(INITIAL * 4, id=id)
        self.soft_wrap = soft_wrap
        self.indent_type = "tabs"


class TexMacsApp(App[None]):
    def compose(self) -> ComposeResult:
        with Horizontal():
            yield TexMacs(True, id="wrapped")
            yield TexMacs(False, id="non-wrapped")

    @on(TextArea.Changed)
    def compare(self, event: TextArea.Changed) -> None:
        self.query_one(
            "#non-wrapped" if event.control.id == "wrapped" else "#wrapped", TexMacs
        ).text = event.text_area.text


if __name__ == "__main__":
    TexMacsApp().run()

### texmacs.py ends here
