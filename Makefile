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
	@$(python) $@.py

.PHONY: setup
setup:				# Install all dependencies
	pipenv sync --dev

.PHONY: resetup
resetup:			# Recreate the virtual environment from scratch
	rm -rf $(shell pipenv --venv)
	pipenv sync --dev

.PHONY: depsoutdated
depsoutdated:			# Show a list of outdated dependencies
	pipenv update --outdated

.PHONY: depsupdate
depsupdate:			# Update all dependencies
	pipenv update --dev

.PHONY: depsshow
depsshow:			# Show the dependency graph
	pipenv graph

### Makefile ends here
