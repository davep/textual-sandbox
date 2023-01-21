from textual.app        import App, ComposeResult
from textual.containers import Vertical
from textual.widgets    import Header, Footer, Label

class AsyncClickApp( App[ None ] ):

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Label( "[@click=app.sync]Sync Action[/] [@click=app.async]Async Action[/]")
        yield Vertical()
        yield Footer()

    def action_sync( self ) -> None:
        self.query_one( Vertical ).mount( Label( "Via Sync Action" ) )

    async def action_async( self ) -> None:
        await self.query_one( Vertical ).mount( Label( "Via Async Action" ) )

if __name__ == "__main__":
    AsyncClickApp().run()
