.PHONY: setup run test install-deps clean

setup:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

run:
	bash scripts/run_instacart.sh

test:
	bash scripts/test_instacart.sh

install-deps:
	. venv/bin/activate && pip install -r requirements.txt

clean:
	rm -rf venv __pycache__
