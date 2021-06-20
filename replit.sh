#!/usr/bin/env sh
pip3 install --upgrade pip
pip3 install pytest
pytest tests/
python3 src/main.py
