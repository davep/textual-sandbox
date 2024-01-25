"""Suspend-related signal testing."""

from os import kill, getpid
from signal import signal, SIGTTIN, SIGCONT, SIGTSTP, SIGSTOP

def sigttin_handler(*_) -> None:
    print("SIGTTIN")

def sigcont_handler(*_) -> None:
    print("SIGCONT")

def sigtstp_handler(*_) -> None:
    print("SIGTSTP")
    kill(getpid(), SIGSTOP)

def run() -> None:
    signal(SIGTSTP, sigtstp_handler)
    signal(SIGTTIN, sigttin_handler)
    signal(SIGCONT, sigcont_handler)
    for n in range(10_000):
        print(n)
        input("Press Enter")

if __name__ == "__main__":
    run()

### signal_tester.py ends here
