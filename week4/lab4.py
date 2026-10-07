sonnets = []

with open("week4/shakespere.txt", "r") as file:
    lines = file.readlines()

i = 0

while i < len(lines):
    line = lines[i].strip()

    # Skip empty lines
    if line == "":
        i += 1
        continue

    # Roman nimeral = sonnet number 
    roman_number = line

    # Move to the first line of the sonnet 
    i += 1

    poem_lines = []
    