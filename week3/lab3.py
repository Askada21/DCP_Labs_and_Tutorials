with open("data/oneills.abc", "r", encoding="latin-1") as f:
    lines = f.readlines()

# Loading the file
# Print the total number of lines
print("\nTotal number of lines: ")
print(len(lines))
# Print the first 20 lines to see the structure
print("\nFirst 20 lines: ")
print(lines[:20])
print()
# Print the last 10 lines
print("\nThe last 10 lines: ")
print(lines[-10:])
# Print the file backwards!
print("\nBackwards: ")
print(lines[::-1])

# Parse tunes into a list of dictionaries
tunes = []
in_tune = False

for line in lines:

    # Start of a new tune
    if line.startswith("X:"):
        in_tune = True

        tune = {
            "X": line[2:].strip(),
            "title": None,
            "alt_title": None,
            "tune_type": None,
            "key": None,
            "notation": line,
        }

    elif in_tune:

        # End of the tune
        if line.strip() == "":
            tunes.append(tune)
            in_tune = False

        else:
            # Add line to the full notation
            tune["notation"] += line

            # Title
            if line.startswith("T:") or line.startswith("t:"):
                if tune["title"] is None:
                    tune["title"] = line[2:].strip()
                else:
                    tune["alt_title"] = line[2:].strip()

            # Tune type
            elif line.startswith("R:"):
                tune["tune_type"] = line[2:].strip()

            # Key
            elif line.startswith("K:"):
                tune["key"] = line[2:].strip()

# Add the last tune if the file does not end with a blank line
if in_tune:
    tunes.append(tune)

# Print number of tunes
print(f"\nFound {len(tunes)} tunes")

# Print first and last tune
print("\nFirst tune:")
print(tunes[0])

print("\nLast tune:")
print(tunes[-1])

# Print all titles and alternative titles
print("\nTitles:")

for tune in tunes:
    print("Title:", tune["title"])
    print("Alt title:", tune["alt_title"])

# Additional challenges
# Count all reels
reels = len([tune for tune in tunes if tune["tune_type"] == "reel"])
print("\nNumber of reels:", reels)

# Count all jigs
jigs = len([tune for tune in tunes if tune["tune_type"] == "jig"])
print("Number of jigs:", jigs)

# List all tunes with "Green" in the title
green_tunes = [
    tune for tune in tunes if tune["title"] is not None and "Green" in tune["title"]
]

print("\nTunes with Green in the title:")
for tune in green_tunes:
    print(tune["title"])
