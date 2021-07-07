#!/usr/bin/env python3
from random import randint
from brain_games.engine import game_engine


def find_common_divisor(first_num, second_num):
    nod = 1
    min_num = min(first_num, second_num)
    for i in range(2, min_num + 1):
        if first_num % i == 0 and second_num % i == 0:
            nod = i
    return nod


def get_qa():
    questions_list = []
    for i in range(3):
        first_num = randint(1, 100)
        second_num = randint(1, 100)
        correct_answer = str(find_common_divisor(first_num, second_num))
        task = '{} {}'.format(first_num, second_num)
        questions_list.append((task, correct_answer))
    return questions_list


def main():
    description = 'Find the greatest common divisor of given numbers.'
    game_questions = get_qa()
    game_engine(description=description, questions=game_questions)


if __name__ == '__main__':
    main()
