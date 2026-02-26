.PHONY: setup run install-deps clean

setup:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

run:
	. venv/bin/activate && python3 src/main.py

install-deps:
	. venv/bin/activate && pip install -r requirements.txt

clean:
	rm -rf venv __pycache__
