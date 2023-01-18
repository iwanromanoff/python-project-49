import random


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    """
    Check the evenness of the number.
    Args:
        number (int): Random number.
    Returns:
        bool
    """
    return number % 2 == 0


def get_game_data():
    """
    Collect game data.
    Returns:
        DESCRIPTION (str): Game rules.
        data (list): Сontains a question and an answer.
    """
    question = random.randint(1, 100)
    true_answer = 'yes' if is_even(question) else 'no'

    return (question, true_answer)
