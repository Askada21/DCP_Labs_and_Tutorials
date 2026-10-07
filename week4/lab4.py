# Part 1
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
import random

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
