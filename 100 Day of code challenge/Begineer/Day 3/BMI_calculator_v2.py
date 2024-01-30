#Exercise 3

#height
height = float(input("enter your height in m: "))
#weight
weight = int(input("enter your weight in kg: "))

#BMI formula
result = weight / height ** 2
result = round(result,2)

if result <= 18.5:
    print(f"Your BMI {result} and you are underweight.")
elif result >= 18.5:
    print(f"Your BMI {result} and you are a normal weight.")
elif result > 25:
    print(f"Your BMI {result} and you are owerweight.")
elif result > 30:
    print(f"Your BMI {result} and you are obese.")
else:
    print(f"Your BMI {result} and you are clinically obese.")