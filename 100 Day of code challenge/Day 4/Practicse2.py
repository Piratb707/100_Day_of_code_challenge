
import random

names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(", ")
print(f"You enter these names {names}")

names_len = len(names)
print(f"Numbers of names {names_len}")
chosen = random.randint(1, names_len)
input("Press enter to START!")
print(f"{names[chosen]} is going to buy the meal today!")