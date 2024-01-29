import itertools

election = {1: "Barb", 2: "Karen", 3: "Erin"}
for p in itertools.permutations(election):
    print(p)

for p1 in itertools.permutations(election.values()):
    print(p1)

colors_for_painting = ["Red", "Blue", "Purple", "Orange", "Yellow", "Pink"]
for c in itertools.combinations(colors_for_painting, 3):
    print(c)

