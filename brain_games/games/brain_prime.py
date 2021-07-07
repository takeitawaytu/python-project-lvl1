#!/usr/bin/env python3
from random import randint
from brain_games.engine import game_engine


def is_prime(number):
    if number <= 1:
        return 'no'
    for i in range(2, number):
        if number % i == 0:
            return 'no'
    return 'yes'



def get_qa():
    questions_list = []
    for i in range(3):
        number = randint(1, 100)
        correct_answer = is_prime(number)
        questions_list.append((number, correct_answer))
    return questions_list


def main():
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game_questions = get_qa()
    game_engine(description=description, questions=game_questions)


if __name__ == '__main__':
    main()
