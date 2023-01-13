#!/usr/bin/env python3

import prompt
from random import randint


min_num = 1
max_num = 100


def is_even(num):
    return num % 2 == 0


def run_game():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    trying = 0

    while trying < 3:
        random_num = randint(min_num, max_num)
        correct = 'yes' if is_even(random_num) else 'no'
        print(f'Question: {random_num}')
        answer = prompt.string('Your answer: ')
        if answer != correct:
            print(f'{answer} is wrong answer ;(. Correct answer was {correct}.')
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
        trying += 1

    print(f"Congratulations, {name}!")


def main():
    run_game()


if __name__ == '__main__':
    main()
