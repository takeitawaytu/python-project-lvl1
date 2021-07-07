#!/usr/bin/env python3
from random import randint
from brain_games.engine import game_engine


def get_missing_num(start_num):
    progression_list = []
    nums_range = randint(5, 10)
    rand_list_index = randint(0, nums_range - 1)
    num = start_num
    step = randint(1, 10)
    for i in range(nums_range):
        progression_list.append(num)
        num += step
    correct_answer = str(progression_list[rand_list_index])
    progression_list[rand_list_index] = '..'
    data = ' '.join(map(str, progression_list))
    return data, correct_answer


def get_qa():
    questions_list = []
    for i in range(3):
        start_num = randint(1, 100)
        task, correct_answer = get_missing_num(start_num)
        questions_list.append((task, str(correct_answer)))
    return questions_list


def main():
    description = 'What number is missing in the progression?'
    game_questions = get_qa()
    game_engine(description=description, questions=game_questions)


if __name__ == '__main__':
    main()