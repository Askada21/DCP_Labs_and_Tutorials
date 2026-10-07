# Part 1
import random
sonnets = []

with open("week4/shakespere.txt", "r", encoding="utf-8-sig") as file:
    lines = file.readlines()

roman_number = None
poem_lines = []

for line in lines:
    line = line.strip()

    # Ignore empty lines
    if line == "":
        continue

    # Check if the line is a Roman numeral
    if all(letter in "IVXLCDM" for letter in line):

        # Save the previous sonnet
        if roman_number is not None:
            sonnets.append({roman_number: poem_lines})

        # Start a new sonnet
        roman_number = line
        poem_lines = []

    else:
        # Add poetry line to current sonnet
        if roman_number is not None:
            poem_lines.append(line)

# Save the final sonnet
if roman_number is not None:
    sonnets.append({roman_number: poem_lines})

# Print Roman numeral + first line
for sonnet in sonnets:
    for number, lines in sonnet.items():
        print(number, lines[0])

# Part 2
model = {}

for sonnet in sonnets:
    for number, lines in sonnet.items():

        # Turn all 14 lines into one string
        text = " ".join(lines)

        # Make everything lowercase
        words = text.lower().split()

        # Go through the words
        for i in range(len(words)):

            word = words[i]

            # Add the word to the dictionary if it isn't there
            if word not in model:
                model[word] = []

            # If there is another word after this word
            if i + 1 < len(words):
                next_word = words[i + 1]
                model[word].append(next_word)

# Generate poem
print("\nDANI'S POEM\n")

for line_number in range(14):

    current_word = random.choice(list(model.keys()))

    poem_line = [current_word]

    while len(poem_line) < 8:

        possible_words = model[current_word]

        if len(possible_words) == 0:
            break

        next_word = random.choice(possible_words)

        poem_line.append(next_word)

        current_word = next_word

    print(" ".join(poem_line))

# EXTRA - DANI IN ALBANIAN

import random

model_albanian = {}

with open("week4/albanian.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

words = text.split()

# Train DANI
for i in range(len(words)):
    word = words[i]

    if word not in model_albanian:
        model_albanian[word] = []

    if i + 1 < len(words):
        next_word = words[i + 1]
        model_albanian[word].append(next_word)


# Generate poem in Albanian
print("\nDANI IN ALBANIAN")
for line_number in range(14):

    current_word = random.choice(list(model_albanian.keys()))
    poem_line = [current_word]

    while len(poem_line) < 8:

        possible_words = model_albanian[current_word]

        if len(possible_words) == 0:
            break

        next_word = random.choice(possible_words)

        poem_line.append(next_word)
        current_word = next_word

    print(" ".join(poem_line))
