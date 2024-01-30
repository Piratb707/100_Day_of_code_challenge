#Exercise 4

year = int(input("Which year do you wand to check?:  "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap!")
        else:
            print("Not Leap!")
    else:
        print("Not Leap!")
else:
    print("Not Leap!")