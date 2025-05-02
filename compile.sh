#!/bin/bash

source venv/bin/activate
pip-compile -o requirements.txt
python3 -m pip install -r requirements.txt