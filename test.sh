#!/bin/sh
set -e
flake8 src/
black src/
pytest src/
mypy src/