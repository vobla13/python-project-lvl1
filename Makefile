install: # Run <poetry install> command
	poetry install


brain-games: # Run <brain-games> module
	poetry run brain-games


.PHONY: install test lint selfcheck check build
