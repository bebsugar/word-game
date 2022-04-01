from function.utils import get_random_word


def main():
    random_word = get_random_word()
    word = random_word[0]
    translation = random_word[1]
    guess = input(f'{word}: ')
    if guess == translation:
        print('Correct!')
        main()
    else:
        print(f'Incorrect. The translation of the word: {translation}')
        main()


main()
