#!/usr/bin/bash
set -e

path=`dirname $0`
cd "$path"
.venv/bin/python client/control/clock.py
