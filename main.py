import random

words = ["hacker", "bounty", "hunter"]

chosen_word = random.choice(words)

print(chosen_word)

display = []

for letter in chosen_word:
    display += "_"

game_over = False
num_of_guess = 0

while not game_over:

    num_of_guess += 1
    input_letter = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == input_letter:
            display[position] = input_letter
    
    print(display)

    if num_of_guess == 7:
        game_over = True
        print("You lose")
        break
    
    if "_" not in display:
        game_over = True
        print("You win")

print("game complete")