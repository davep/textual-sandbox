run     := pipenv run
python  := $(run) python
textual := $(run) textual

.PHONY: all
all:
	$(textual)

.PHONY: borders
borders:
	$(textual) borders

.PHONY: console
console:
	$(textual) console

.PHONY: easing
easing:
	$(textual) easing

.PHONY: demo
demo:
	$(python) -m textual

.PHONY: docs
docs:
	open https://textual.textualize.io

.PHONY: repl
repl:
	$(run) python

%::
	@$(textual) run $@.py

### Makefile ends here
