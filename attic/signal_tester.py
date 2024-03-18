"""Suspend-related signal testing."""

from os import getpid, kill
from signal import SIG_DFL, SIGCONT, SIGSTOP, SIGTSTP, SIGTTIN, SIGTTOU, signal
from sys import __stdout__ as stdout
from termios import TCSANOW, error, tcgetattr, tcsetattr


def disallowed_resume(*_) -> None:
    kill(getpid(), SIGSTOP)


def alt_screen(enable: bool) -> None:
    if enable:
        signal(SIGTTOU, disallowed_resume)
        signal(SIGTTIN, disallowed_resume)
        try:
            tcsetattr(stdout.fileno(), TCSANOW, tcgetattr(stdout.fileno()))
        except error:
            return
        finally:
            signal(SIGTTOU, SIG_DFL)
            signal(SIGTTIN, SIG_DFL)
    print("\x1b[?1049h\x1b[?25l" if enable else "\x1b[?1049l\x1b[?25h")


def sigcont_handler(*_) -> None:
    print("CONT")
    alt_screen(True)


def sigtstp_handler(*_) -> None:
    alt_screen(False)
    kill(getpid(), SIGSTOP)


def run() -> None:
    alt_screen(True)
    signal(SIGTSTP, sigtstp_handler)
    signal(SIGCONT, sigcont_handler)
    for n in range(10_000):
        print(n)
        try:
            input("Press Enter")
        except (EOFError, KeyboardInterrupt):
            break
    alt_screen(False)


if __name__ == "__main__":
    run()

### signal_tester.py ends here
