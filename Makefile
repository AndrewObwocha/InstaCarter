.PHONY: setup run clean

setup:
    python3 -m venv venv
    . venv/bin/activate && pip install -r requirements.txt

run:
    . venv/bin/activate && python3 main.py

install-deps:
    . venv/bin/activate && pip install -r requirements.txt

clean:
    rm -rf venv __pycache__
