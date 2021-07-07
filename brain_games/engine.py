import prompt
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet


def game_engine(description='', questions=''):
    greet()
    name = welcome_user()
    print(description)
    for question in questions:
        data, correct_answer = question
        print('Question: {}'.format(data))
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print('''"{}" is wrong answer ;(.
            Correct answer was "{}".'''.format(answer, correct_answer))
            return print('Let\'s try again, {}!'.format(name))
        elif answer == correct_answer:
            print('Correct!')
    return print('Congratulations, {}!'.format(name))


def main():
    game_engine()


if __name__ == '__main__':
    main()
