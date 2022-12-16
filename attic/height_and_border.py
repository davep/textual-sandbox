from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static

class TestApp( App[ None ] ):

    CSS = "Horizontal { height: 1fr;}\n.border-calc {box-sizing: content-box; }\nStatic { border: solid red}\n" + "\n".join(
        f"Static.box-{n} {{ width: {(1+n)*2}; height: {1+n};}}"
        for n in range( 10 )
    )

    def compose( self ) -> ComposeResult:
        yield Horizontal(
            *[ Static( str(n), classes=f"box-{n}" ) for n in range( 10 ) ]
        )
        yield Horizontal(
            *[ Static( str(n), classes=f"border-calc box-{n}" ) for n in range( 10 ) ]
        )

if __name__ == "__main__":
    TestApp().run()

