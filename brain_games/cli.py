import prompt


def welcome_user():
    name = prompt.string('May i have your name? ')
    return print('Hello, {}!'.format(name))


def main():
    welcome_user()


if __name__ == '__main__':
    main()
