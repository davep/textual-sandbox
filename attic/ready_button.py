from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Button

class MyApp(App):
    ready = reactive(False,init=False)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'enable':
            self.ready = True

    def watch_ready(self, ready: bool) -> None:
        self.query_one( "#do_the_thing", Button).disabled = not ready

    def compose(self) -> ComposeResult:
        yield Button('Enable', variant='primary', id='enable')
        yield Button('Do the thing', variant='primary', id='do_the_thing', disabled=not self.ready)

if __name__ == '__main__':
    MyApp().run()

