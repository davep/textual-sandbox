from textual.app import App
from textual.screen import ModalScreen

class SomeScreen(ModalScreen[str]):
    pass

class SomeApp(App[int]):
    pass
