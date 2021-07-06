#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet


def check_even_num():
	name = welcome_user()
	print('Answer "yes" if the number is even, otherwise answer "no".')
	for i in range(4):
		if i < 3:
			n = randint(1, 99)
			print('Question: {}'.format(n))
			answer = prompt.string('Your answer: ')
			if n % 2 == 0 and answer == 'yes':
				print('Correct!')
			elif n % 2 == 0 and answer != 'yes':
				print('"no" is wrong answer ;(. Correct answer was "yes".')
				print('Let\'s try again, {}!'.format(name))
				break
			elif n % 2 != 0 and answer == 'no':
				print('Correct!')
			elif n % 2 != 0 and answer != 'no':
				print('"yes" is wrong answer ;(. Correct answer was "no".')
				print('Let\'s try again, {}!'.format(name))
				break
		elif i == 3:
			print('Congratulations, {}!'.format(name))


def main():
	greet()
	check_even_num()


if __name__ == '__main__':
	main()

        