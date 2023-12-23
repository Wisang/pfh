import random

words = ["hacker", "bounty", "hunter"]

chosen_word = random.choice(words)

print(chosen_word)

display = []

for letter in chosen_word:
    display += "_"

while "_" in display:
    input_letter = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == input_letter:
            display[i] = input_letter

    print(display)

print("game complete")