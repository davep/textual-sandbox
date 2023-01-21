"""https://github.com/Textualize/textual/issues/1634"""

from textual.app        import App, ComposeResult
from textual.containers import Vertical
from textual.widgets    import Header, Footer, Label

class Output( Vertical ):

    async def clear( self ) -> None:
        await self.query( "*" ).remove()

    async def populate( self ) -> None:
        await self.clear()
        await self.mount( *[
            Label( f"[@click=app.populate]Repopulate this widget[/] {n}")
            for n in range( 20 )
        ] )

    async def on_mount( self ) -> None:
        await self.populate()

class SelfRemoveApp( App[ None ] ):

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Output()
        yield Footer()

    async def action_populate( self ) -> None:
        await self.query_one( Output ).populate()

if __name__ == "__main__":
    SelfRemoveApp().run()
