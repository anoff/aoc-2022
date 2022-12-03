#!/bin/sh
set -e
black src/
pytest src/
mypy src/