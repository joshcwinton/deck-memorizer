import os
from random import shuffle

suits = ['D', 'H', 'C', 'S']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = []

for suit in suits:
    for value in values:
        deck.append(value + suit)

size = int(input("Enter game size: "))

shuffle(deck)
deck = deck[:size]
print(deck)

input("Press ENTER")

os.system('cls' if os.name == 'nt' else 'clear')

solved = False
guesses = []
idx = 0

while not solved:
    print(guesses)
    guess = input("Enter next card")
    if guess == deck[idx]:
        print("Correct!")
        guesses.append(guess)
        idx += 1
        if idx == 53:
            solved = True
            print("You Win!")
    else:
        print("Try again")

