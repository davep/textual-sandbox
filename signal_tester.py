"""Suspend-related signal testing."""

from os import kill, getpid
from signal import SIGTTOU, signal, SIGTTIN, SIGCONT, SIGTSTP, SIGSTOP

def sigttin_handler(*_) -> None:
    print("SIGTTIN - This means we got placed in the bg and we're trying to get input")
    print("SIGTTIN - We can't keep doing that so we're going to send SIGSTOP again")
    kill(getpid(), SIGSTOP)

def sigttou_handler(*_) -> None:
    print("SIGTTOU")

def sigcont_handler(*_) -> None:
    print("SIGCONT - We're back! This will happen before the final line in SIGTSTP")

def sigtstp_handler(*_) -> None:
    print("SIGTSTP - This is where we'd pause the Textual app")
    print("SIGTSTP - Now that we've done that, we'll send SIGSTOP itself to the app")
    kill(getpid(), SIGSTOP)
    print("SIGTSTP - THis is after: kill(getpid(), SIGSTOP)")

def run() -> None:
    signal(SIGTSTP, sigtstp_handler)
    signal(SIGTTIN, sigttin_handler)
    signal(SIGTTOU, sigttou_handler)
    signal(SIGCONT, sigcont_handler)
    for n in range(10_000):
        print(n)
        input("Press Enter")

if __name__ == "__main__":
    run()

### signal_tester.py ends here
