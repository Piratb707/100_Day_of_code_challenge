
row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]

map = [row1, row2, row3]

print(f"   1    2    3\n1{row1}\n2{row2}\n3{row3}")

position = input("Where do you want to put the tresure?:  ")
position1 = int(position[-2])
position1 = position1 -1

position2 = int(position[-1])
position2 = position2 -1

map[position2][position1] = "X"

print(f"   1    2    3\n1{row1}\n2{row2}\n3{row3}")