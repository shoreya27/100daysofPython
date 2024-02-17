import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.

display = ['_']*len(chosen_word)
guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;

for index in range(0, len(chosen_word)):
    if chosen_word[index] == guess:
        display[index] = guess

print(display)
