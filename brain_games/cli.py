import prompt


def welcome_user():
    user_name = prompt.string('May I have your name? ')
    message = f'Hello, {user_name}!'
    print(message)
    return user_name


def congrats(user_name):
    message = f'Congratulations, {user_name}!'
    print(message)


def try_again(user_name):
    message = f'Let\'s try again, {user_name}!'
    print(message)


def question(question_text):
    answer = prompt.string(f'{question_text} ')
    return answer
