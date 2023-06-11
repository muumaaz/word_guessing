import random

INITIAL_GUESSES = 8
LEXICON_FILE = "Lexicon.txt"

def get_word():
    with open(LEXICON_FILE, 'r') as file:
        word_list = [line.strip() for line in file.readlines()]
    return random.choice(word_list)

def play_game():
    secret_word = get_word()
    guessed_word = ['-'] * len(secret_word)
    guesses_left = INITIAL_GUESSES

    while True:
        print_word(guessed_word)
        print(f"You have {guesses_left} guesses left")
        guess = input("Type a single letter here, then press enter: ").upper()

        if len(guess) != 1:
            print("Guess should only be a single character.")
            continue

        if guess in secret_word:
            update_guessed_word(secret_word, guessed_word, guess)
            print("That guess is correct.")
        else:
            print(f"There are no {guess}'s in the word.")
            guesses_left -= 1

        if is_word_guessed(guessed_word):
            print(f"Congratulations, the word is: {secret_word}")
            break

        if guesses_left == 0:
            print(f"Sorry, you lost. The secret word was: {secret_word}")
            break

def print_word(word):
    print("The word now looks like this:", " ".join(word))

def update_guessed_word(secret_word, guessed_word, guess):
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            guessed_word[i] = guess

def is_word_guessed(word):
    return '-' not in word

def main():
    play_game()

if __name__ == '__main__':
    main()

