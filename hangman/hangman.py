import random


class Hangman:
    def __init__(self, guess_set: set, lives: int):
        self.word = random.sample(guess_set, 1)[0]
        self.lives = lives
        self.hint = '-' * len(self.word)
        self.guesses = set()

    def start(self) -> None:
        while True:
            print('H A N G M A N')
            action = input('Type "play" to play the game, "exit" to quit:')

            if action == 'play':
                self.__game_loop()
            else:
                break

    def __game_loop(self) -> None:
        while (self.lives > 0) and ('-' in self.hint):
            print('\n' + self.hint)
            user_guess: str = input('Input a letter:')

            if self.__is_input_valid(user_guess) is False:
                continue
            elif user_guess in self.word:
                self.__correct_guess(user_guess)
            else:
                self.__wrong_guess()

            self.guesses.add(user_guess)

        self.__finish()

    def __is_input_valid(self, user_guess: str) -> bool:
        if len(user_guess) is not 1:
            print('You should input a single letter')
            return False
        if not user_guess.islower():
            print('It is not an ASCII lowercase letter')
            return False
        if user_guess in self.guesses:
            print('You already typed this letter')
            return False
        return True

    def __correct_guess(self, user_guess: str) -> None:
        new_hint: list = list(self.hint)

        for i in range(len(self.word)):
            if user_guess is self.word[i]:
                new_hint[i] = user_guess

        self.hint = ''.join(new_hint)

    def __wrong_guess(self) -> None:
        print('No such letter in the word')
        self.lives -= 1

    def __finish(self) -> None:
        if '-' not in self.hint:
            print(f'You guessed the word {self.word}!\nYou survived!')
        elif self.lives is 0:
            print('You are hanged!')


if __name__ == '__main__':
    hangman = Hangman({'python', 'java', 'kotlin', 'javascript'}, 8)
    hangman.start()
