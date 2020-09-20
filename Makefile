coverage:  ## Run tests with coverage
	coverage erase
	coverage run --include=statprly/* -m pytest -ra
	coverage report -m

deps:  ## Install dependencies
	pip install -r requirements/development.txt

lint:  ## Lint and static-check
	flake8 dadata
	pylint dadata
	mypy dadata

push:  ## Push code with tags
	git push && git push --tags

test:  ## Run tests
	pytest -ra
