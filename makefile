.PHONY: deps
deps:
	pip install -r requirements.txt

.PHONY: run
run:
	python -m main

.PHONY: get-model
get-model:
	python -m bin.download_model_from_huggingface_hub
