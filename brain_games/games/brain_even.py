#!/usr/bin/env python3
from random import randint
from brain_games.engine import game_engine


def is_even(number):
	if number % 2 == 0:
		return 'yes'
	else:
		return 'no'


def get_qa():
	questions_list = []
	for i in range(3):
		number = randint(1, 100)
		correct_answer = is_even(number)
		questions_list.append((number, correct_answer))
	return questions_list


def main():
	game_questions = get_qa()
	game_engine(questions=game_questions)


if __name__ == '__main__':
	main()
