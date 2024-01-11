#Exercise 2
#BMI Calculator

#height
height = float(input("enter your height in m: "))
#weight
weight = int(input("enter your weight in kg: "))

#BMI formula
result = weight / height ** 2

#Result
print(int(result))