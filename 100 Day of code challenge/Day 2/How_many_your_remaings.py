#Exercise 3
#Your life in weeks

age = input("What is your current age?: ")

age = int(age)
difference_age = 90 - age

days = difference_age * 365
weeks = difference_age * 52
months = difference_age * 12
years = difference_age

message = f"You have {days}, {weeks} weeks, {months} months, and {years} years left"

print(message)