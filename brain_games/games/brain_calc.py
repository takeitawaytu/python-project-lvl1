#!/usr/bin/env python3
from random import randint, choice
from brain_games.engine import game_engine


def calc(first_num, second_num, operator):
    if operator == '+':
        return first_num + second_num
    elif operator == '-':
        return first_num - second_num
    elif operator == '*':
        return first_num * second_num


def get_qa():
    questions_list = []
    for i in range(3):
        first_num = randint(1, 100)
        second_num = randint(1, 100)
        random_operator = choice(['+', '-', '*'])
        correct_answer = str(calc(first_num, second_num, random_operator))
        task = '{} {} {}'.format(first_num, random_operator, second_num)
        questions_list.append((task, correct_answer))
    return questions_list


def main():
    description = 'What is the result of the expression?'
    game_questions = get_qa()
    game_engine(description=description, questions=game_questions)


if __name__ == '__main__':
    main()
