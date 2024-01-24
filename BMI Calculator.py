# This is a body mass index calculator

# height and weight are the required inputs

height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

# The body mass index is the result from the division of weight by height squared
BMI = round(weight / (height**2))


if BMI < 18.5:
    print(f" Your bmi  is {BMI},you are under weight")
elif 18.5 < BMI < 25:
    print(f" Your bmi  is {BMI},your weight is Normal")
elif 25 < BMI < 30:
    print(f" Your bmi  is {BMI},you are Overweight")
elif 30 < BMI < 35:
    print(f" Your bmi  is {BMI},you are Obese")
else:
    print(f" Your bmi  is {BMI},you are Clinically Obese")