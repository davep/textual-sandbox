from asyncio import sleep
from typing import AsyncIterator
from functools import partial
from itertools import cycle
from random import random


from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.screen import Screen
from textual.widgets import Label

from textual.command_palette import CommandPalette, CommandSource, CommandSourceHit

from rich.text import Text

class TotallyFakeCommandSource(CommandSource):
    """Really, this isn't going to be the UI. Not even close."""

    DATA = """\
A bird in the hand is worth two in the bush.
A chain is only as strong as its weakest link.
A fool and his money are soon parted.
A man's reach should exceed his grasp.
A picture is worth a thousand words.
A stitch in time saves nine.
Absence makes the heart grow fonder.
Actions speak louder than words.
Although never is often better than *right* now.
Although practicality beats purity.
Although that way may not be obvious at first unless you're Dutch.
Anything is possible.
Be grateful for what you have.
Be kind to yourself and to others.
Be open to new experiences.
Be the change you want to see in the world.
Beautiful is better than ugly.
Believe in yourself.
Better late than never.
Complex is better than complicated.
Curiosity killed the cat.
Don't judge a book by its cover.
Don't put all your eggs in one basket.
Enjoy the ride.
Errors should never pass silently.
Explicit is better than implicit.
Flat is better than nested.
Follow your dreams.
Follow your heart.
Forgive yourself and others.
Fortune favors the bold.
He who hesitates is lost.
If the implementation is easy to explain, it may be a good idea.
If the implementation is hard to explain, it's a bad idea.
If wishes were horses, beggars would ride.
If you can't beat them, join them.
If you can't do it right, don't do it at all.
If you don't like something, change it. If you can't change it, change your attitude.
If you want something you've never had, you have to do something you've never done.
In the face of ambiguity, refuse the temptation to guess.
It's better to have loved and lost than to have never loved at all.
It's not over until the fat lady sings.
Knowledge is power.
Let go of the past and focus on the present.
Life is a journey, not a destination.
Live each day to the fullest.
Live your dreams.
Look before you leap.
Make a difference.
Make the most of every moment.
Namespaces are one honking great idea -- let's do more of those!
Never give up.
Never say never.
No man is an island.
No pain, no gain.
Now is better than never.
One for all and all for one.
One man's trash is another man's treasure.
Readability counts.
Silence is golden.
Simple is better than complex.
Sparse is better than dense.
Special cases aren't special enough to break the rules.
The answer is always in the last place you look.
The best defense is a good offense.
The best is yet to come.
The best way to predict the future is to create it.
The early bird gets the worm.
The exception proves the rule.
The future belongs to those who believe in the beauty of their dreams.
The future is not an inheritance, it is an opportunity and an obligation.
The grass is always greener on the other side.
The journey is the destination.
The journey of a thousand miles begins with a single step.
The more things change, the more they stay the same.
The only person you are destined to become is the person you decide to be.
The only way to do great work is to love what you do.
The past is a foreign country, they do things differently there.
The pen is mightier than the sword.
The road to hell is paved with good intentions.
The sky is the limit.
The squeaky wheel gets the grease.
The whole is greater than the sum of its parts.
The world is a beautiful place, don't be afraid to explore it.
The world is your oyster.
There is always something to be grateful for.
There should be one-- and preferably only one --obvious way to do it.
There's no such thing as a free lunch.
Too many cooks spoil the broth.
United we stand, divided we fall.
Unless explicitly silenced.
We are all in this together.
What doesn't kill you makes you stronger.
When in doubt, consult a chicken.
You are the master of your own destiny.
You can't have your cake and eat it too.
You can't teach an old dog new tricks.
    """.strip().splitlines()

    async def hunt_for(self, user_input: str) -> AsyncIterator[CommandSourceHit]:
        """A request to hunt for commands relevant to the given user input.

        Args:
            user_input: The user input to be matched.
        """
        matcher = self.matcher(user_input)
        for candidate in self.DATA:
            await sleep(random() / 10)
            if matcher.match(candidate):
                yield CommandSourceHit(
                    matcher.match(candidate),
                    Text.assemble(
                        Text.from_markup("[italic green]notify('[/]"),
                        matcher.highlight(candidate),
                        Text.from_markup("[italic green]')[/]")
                    ),
                    partial(self.screen.notify, candidate),
                    candidate,
                    "Show the selected text as a notification\n"
                    f"I think the current screen is {self.screen!r}\n"
                    f"I think the focused widget is {self.focused!r}\n"
                    f"Match score: {matcher.match(candidate):0.5f}"
                )


class MinibufferApp(App[None]):

    CSS = """
    Grid {
        grid-size: 11;
    }

    CommandPalette > .command-palette--highlight {
        text-style: reverse;
        color: yellow;
    }

    Label {
        width: 1fr;
        height: 1fr;
        content-align: center middle;
        transition: background 220ms linear;
    }

    Label.colour-0 {
        background: #881177;
    }

    Label.colour-1 {
        background: #aa3355;
    }

    Label.colour-2 {
        background: #cc6666;
    }

    Label.colour-3 {
        background: #ee9944;
    }

    Label.colour-4 {
        background: #eedd00;
    }

    Label.colour-5 {
        background: #99dd55;
    }

    Label.colour-6 {
        background: #44dd88;
    }

    Label.colour-7 {
        background: #22ccbb;
    }

    Label.colour-8 {
        background: #00bbcc;
    }

    Label.colour-9 {
        background: #0099cc;
    }

    Label.colour-10 {
        background: #3366bb;
    }

    Label.colour-11 {
        background: #663399;
    }
    """

    def compose(self) -> ComposeResult:
        with Grid():
            colours = cycle(range(12))
            for _ in range(11 * 11):
                yield Label("M-x", classes=f"colour-{next(colours)}")

    async def cycle_background(self, screen: Screen) -> None:
        for label in screen.query(Label):
            _, number = list(label.classes)[0].split("-")
            label.set_classes(f"colour-{(int(number)+1) % 12}")

    def on_mount(self) -> None:
        CommandPalette.run_on_select = False
        CommandPalette.register_source(TotallyFakeCommandSource)
        self.app.set_interval(0.25, partial(self.cycle_background, self.screen))

if __name__ == "__main__":
    MinibufferApp().run()
