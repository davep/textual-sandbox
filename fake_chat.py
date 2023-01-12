"""https://github.com/Textualize/textual/issues/1554"""

from random import sample

from textual.app        import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets    import Header, Footer, TextLog, Label
from textual.binding    import Binding

class ChatPane( Vertical ):

    def compose( self ) -> ComposeResult:
        """Compose the child widgets."""
        yield Label( "Title" )
        yield TextLog( wrap=True )

class FakeChatApp( App[ None ] ):

    CSS = """
    ChatPane {
        border: round cyan;
        width: 1fr;
    }

    ChatPane:focus-within {
        border: double cyan;
    }

    ChatPane Label {
        width: 1fr;
        height: 3;
        border: round red;
    }

    ChatPane TextLog {
        height: 1fr;
        width: 1fr;
    }
    """

    BINDINGS = [
        Binding( "l", "log", "Log something" ),
    ]

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Vertical(
            Horizontal( ChatPane(), ChatPane(), ChatPane() ),
            Horizontal( ChatPane(), ChatPane(), ChatPane() ),
        )
        yield Footer()

    TEXT = list( set( """Python was created in the early 1990s by Guido van Rossum at Stichting
    Mathematisch Centrum (CWI, see http://www.cwi.nl) in the Netherlands
    as a successor of a language called ABC.  Guido remains Python's
    principal author, although it includes many contributions from others.

    In 1995, Guido continued his work on Python at the Corporation for
    National Research Initiatives (CNRI, see http://www.cnri.reston.va.us)
    in Reston, Virginia where he released several versions of the
    software.

    In May 2000, Guido and the Python core development team moved to
    BeOpen.com to form the BeOpen PythonLabs team.  In October of the same
    year, the PythonLabs team moved to Digital Creations, which became
    Zope Corporation.  In 2001, the Python Software Foundation (PSF, see
    https://www.python.org/psf/) was formed, a non-profit organization
    created specifically to own Python-related Intellectual Property.
    Zope Corporation was a sponsoring member of the PSF.

    All Python releases are Open Source (see http://www.opensource.org for
    the Open Source Definition).  Historically, most, but not all, Python
    Hit Return for more, or q (and Return) to quit:
    releases have also been GPL-compatible; the table below summarizes
    the various releases.""".lower().split() ) )

    def action_log( self ):
        if self.focused is not None:
            self.focused.write( " ".join( sample( self.TEXT, 50 ) ) )

if __name__ == "__main__":
    FakeChatApp().run()

### fake_chat.py ends here
