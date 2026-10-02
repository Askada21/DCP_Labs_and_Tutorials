import random
# import pyttsx3
# engine = pyttsx3.init()

arr = ["Liverpool", "Man Utd", "St. Pats", "Bohemians"]
fans = [1, 0, 3, 4]
print(arr)
print()

# Reverse
for i in range(len(arr)-1, -1, -1):
    print(arr[i])
print()

for i in range(len(arr)):
    print(f"{arr[i]} has {fans[i]} fans")
print()

for i, team in enumerate(arr): # enumerate() = "give me the item AND its number".
    print(f"{team} has {fans[i]} fans")
print()

for team in arr:
    print(f"{team}")
print()

for fan in fans:
    print(f"{fan}") 
print()

# Random
num = random.randint(0,10)
while True:
    guess = int(input("Whats the number? "))
    if guess == i:
        print("U guessed")
        break
    else: 
        print("Try again")
  

# engine.say("Hello from the ")