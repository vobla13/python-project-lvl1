import prompt


def welcome_user():
    user_name = prompt.string('May I have your name? ')
    welcome_message = f'Hello, {user_name}!'
    print(welcome_message)
