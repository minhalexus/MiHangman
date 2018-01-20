import random

class hangman():

    def __init__(self,word):
        self.word = word.upper()

    def get_unique_letters(self):
        unique_letters = []
        for i in range (len(self.word)):
            for x in range (65,91):
                if ((self.word[i]) == chr(x) and self.word[i] not in unique_letters):
                    unique_letters.append(self.word[i])
        return unique_letters

    def update_template(self,word, correct_guesses):
        template = ''
        for letter in range (len(word)):
            if (word[letter] in correct_guesses):
                template += word[letter]
            else:
                template += '_'
        return template

    def display(self,guess_word):
        d = ''
        for x in range (len(guess_word)):
            d += guess_word[x] + ' '
        return d

    def correct_prompt(self):
        prompts = ['Bravo!', 'Lucky Guess!', 'Ingenious!', 'Correct!']
        r = random.randint(0,3)
        return prompts[r]

    def incorrect_prompt(self):
        prompts = ['Try Harder!', 'Unlucky!', 'Better Luck Next Guess!', 'Darn!']
        r = random.randint(0,3)
        return prompts[r]


    def game(self):
        unique_letters = self.get_unique_letters()
        correct_guesses = []
        incorrect_guesses = 0
        guess_word = self.update_template(self.word, correct_guesses)
        #print(guess_word)

        while ((guess_word != self.word) and (incorrect_guesses < 6)):

            #print(guess_word)
            self.display(guess_word)
            guess = input('Enter your guess: ').upper()

            if (guess in unique_letters):

                correct_guesses.append(guess)
            else:
                print(self.incorrect_prompt())
                incorrect_guesses += 1

            print()
            guess_word = self.update_template(self.word, correct_guesses)

        if (incorrect_guesses > 5):
            self.display(guess_word)
            print('Game Over, You lose!')
        else:
            print('You Win!')
