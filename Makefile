# Makefile

PYTHON ?= python
PYLINT ?= pylint
NPM ?= npm

SETUP := $(PYTHON) setup.py
APP := ./bin/sample_app

all: build

build: bundle
	$(SETUP) build

bundle:
	cd interface; $(NPM) install
	cd interface; $(NPM) run build

watch:
	cd interface; $(NPM) run watch

dist: all
	$(SETUP) bdist_egg

install: all
	$(SETUP) install

clean:
	$(SETUP) clean
	rm -rf build dist *.egg-info sample_app/static/*.js sample_app/static/*.map

check: all lint test

lint:
	$(PYLINT) sample_app setup

debug:
	$(APP) -d -p 8080

help:
	@echo "Makefile"
	@echo
	@echo "Usage: make [TARGET]"
	@echo
	@echo "Available targets:"
	@echo "  all       (default) Build the project."
	@echo "  build     Build the project."
	@echo "  bundle    Create the JavaScript bundle."
	@echo "  watch     Watch for changes in interface files."
	@echo "  dist      Build distribution package (egg)."
	@echo "  install   Install the package on this system."
	@echo "  clean     Remove all files created by other commands."
	@echo "  check     Performs all code validation checks."
	@echo "  lint      Verifies coding rules using Pylint."
	@echo "  test      Run unit tests."
	@echo "  debug     Run application in debug mode."
	@echo "  help      Show this help."

.PHONY: all build dist install clean check lint test debug
