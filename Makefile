install: # Runs <poetry install>
	poetry install


build: # Runs <poetry build>
	poetry build
	

publish: # Runs <poetry publish --dry-run>
	poetry publish --dry-run


package-install: # Runs <python3 -m pip install --user dist/*.whl>
	python3 -m pip install --user dist/*.whl


brain-games: # Run <brain-games> module
	poetry run brain-games
	

lint: # Check code with Flake8
	poetry run flake8 brain_games


.PHONY: install test lint selfcheck check build
