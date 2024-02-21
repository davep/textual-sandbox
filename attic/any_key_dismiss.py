from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.events import Key
from textual.screen import ModalScreen
from textual.widgets import Static


class AnyKeyScreen(ModalScreen[None]):

    def compose(self) -> ComposeResult:
        with VerticalScroll():
            yield Static(
                "\n".join(
                    [
                        f"{n} on_key and no Binding make Jack a dull boy "
                        for n in range(1000)
                    ]
                )
            )

    def on_key(self, event: Key) -> None:
        if not any(
            bindings.keys.get(event.key) for _, bindings in self.app._binding_chain
        ):
            self.dismiss()


class AnyKeyDismissApp(App[None]):

    def on_mount(self) -> None:
        self.push_screen(AnyKeyScreen())


if __name__ == "__main__":
    AnyKeyDismissApp().run()

### any_key_dismiss.py ends here
