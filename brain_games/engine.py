import prompt


def play_game(game):
    """
    Launch the game interface.
    Args:
        game: Contains game data.
    """
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    name_user = prompt.string('May I have your name? ')
    print(f'Hello, {name_user}!')
    rounds_count = 3

    while rounds_count:
        (question, true_answer) = game.get_game_data()
        print(f'Question: {question}')
        answer_user = prompt.string('Your answer: ')

        if (answer_user == true_answer):
            print('Correct!')
            rounds_count -= 1
        else:
            print(f'"{answer_user}" is wrong answer ;(. Correct answer was "{true_answer}"')
            print(f"Let's try again, {name_user}!")
            return

    print(f'Congratulations, {name_user}!')
