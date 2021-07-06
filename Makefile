#Makefile

build:
	poetry build

publish:
	poetry publish --dry-run

install:
	poetry install
	
brain-games:
	poetry run brain-games
	
package-install:
	python -m pip install --user dist/hexlet_code-0.1.1-py3-none-any.whl
	