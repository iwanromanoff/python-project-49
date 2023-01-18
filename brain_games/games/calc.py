import random
import operator


DESCRIPTION = 'What is the result of the expression?'
operations = [
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
]


def get_game_data():
    """
    Collect game data.
    Returns:
        DESCRIPTION (str): Game rules.
        data (list): Сontains a question and an answer.
    """
    operation, calculate = random.choice(operations)
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)
    true_answer = str(calculate(operand1, operand2))
    question = f'{operand1} {operation} {operand2}'

    return (question, true_answer)
