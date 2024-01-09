#Final project day 2

print("*** Final project of Day 2 ***")
print("Welcome to the tip calculator.")

float_total_bill = float(input("What was the total bill?: $"))

#percent calculating by (sum * 100 / percent)
tip_percent = int(input("What percentage tip would you like to give? 10%, 12%, or 15%: %"))
tip = float_total_bill / 100 * tip_percent

number_of_people = int(input("How many people to split the bill?: "))

result = (float_total_bill + tip) / number_of_people
result = "{:.2f}".format(result)

print(f"Each person should pay: ${result}")