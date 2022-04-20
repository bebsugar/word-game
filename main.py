from function.utils import get_random_word, check_date_exists, insert_row, update_row
from datetime import datetime

total_count = 0
correct_answer_count = 0
date = datetime.today().strftime('%Y-%m-%d')


def main():
    random_word = get_random_word()
    word = random_word[0]
    translation = random_word[1]
    guess = input(f'{word}: ')
    if guess == translation:
        print('Correct!')
        global correct_answer_count
        correct_answer_count += 1

    else:
        print(f'Incorrect. The translation of the word: {translation}')
    global total_count
    total_count += 1

    reply = str(input('Do you want a new word? (y/n) '))
    if reply == 'y':
        main()
    else:
        if check_date_exists(date):
            update_row(total_count, correct_answer_count, date)
        else:
            insert_row(date, total_count, correct_answer_count)


main()
