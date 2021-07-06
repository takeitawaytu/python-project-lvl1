#Makefile

install:
	poetry install
	
brain-games: install
	poetry run brain-games
	