#Step 5

import random
from hangman_words import word_list
from hangman_art import logo, stages

# Creating a big word list for making game interesting
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Show the Logo of the game
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f'You already guessed this {guess} letter earlier.')
        continue
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f'This "{guess}" letter does not exist in word, you loose a life.')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    print(stages[lives])

        #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")