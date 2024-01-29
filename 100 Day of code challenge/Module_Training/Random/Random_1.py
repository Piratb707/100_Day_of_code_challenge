import random

print(random.random())
decider = random.randrange(2)
if decider == 0:
    print("HEADS")
else:
    print("TAILS")
print(decider)

print("You rolled a " + str(random.randrange(1, 7)))
print(f"You rolled a {random.randrange(1, 7)}")

lotteryWinners = random.sample(range(100), 5)
print(lotteryWinners)

possible_pets = ['cat', 'dog', 'fish']
print(random.choice(possible_pets))

cards = ['Jack','Queen','King','Ace']
random.shuffle(cards)
print(cards)

