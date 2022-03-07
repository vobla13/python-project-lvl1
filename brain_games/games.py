from brain_games.cli import welcome_user, congrats, try_again, question
from random import randint


# Even game
def even_game():
    user = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    win_count: int = 3

    while win_count != 0:
        number = randint(0, 100)
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        print(f'Question: {number}')
        user_answer = question('Your answer:')

        if user_answer == correct_answer:
            print('Correct!')
            win_count -= 1
            if win_count == 0:
                congrats(user)
                break
        else:
            wrong_message = f'\'{user_answer}\' is wrong answer ;('
            correct_answer = f'Correct answer was \'{correct_answer}\''
            print(wrong_message + correct_answer)
            try_again(user)
            break
