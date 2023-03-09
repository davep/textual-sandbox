from textual.app        import App, ComposeResult
from textual.widgets    import Header, Footer, MarkdownViewer

EXAMPLE = """
# This is heading 1

## This is heading 2

### This is heading 3

#### This is heading 4

##### This is heading 5

###### This is heading 6

* Bullet item 1
    * Bullet item 1
    * Bullet item 2
        * Bullet item 1
        * Bullet item 2
            * Bullet item 1
            * Bullet item 2
                * Bullet item 1
                * Bullet item 2
                    * Bullet item 1
                    * Bullet item 2
                        * Bullet item 1
                        * Bullet item 2
* Bullet item 2
* Bullet item 3
* Bullet item 4
* Bullet item 5
* Bullet item 6
* Bullet item 7
* Bullet item 8
* Bullet item 9
* Bullet item 10

1. List 1
    1. SubList 1
    1. SubList 1
    1. SubList 1
    1. SubList 1
    1. SubList 1
1. List 2
1. List 3
1. List 4
1. List 5
1. List 6
1. List 7
1. List 8
1. List 9
1. List 10

"""

class MarkdownViewerApp( App[ None ] ):

    def compose( self ) -> ComposeResult:
        yield Header()
        yield MarkdownViewer( EXAMPLE )
        yield Footer()

if __name__ == "__main__":
    MarkdownViewerApp().run()
