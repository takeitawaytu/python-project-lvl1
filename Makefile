#Makefile

build:
	poetry build

publish:
	poetry publish --dry-run

install:
	poetry install
	
brain-games:
	poetry run brain-games
	
brain-even:
	poetry run brain-even
	
package-install:
	python -m pip install --user dist/hexlet_code-0.1.3-py3-none-any.whl
	
lint:
	poetry run flake8 brain_games
	