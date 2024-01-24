# This is a body mass index calculator
# height and weight are the required inputs
# The body mass index is the result from the division of weight by height squared

def bmi_calc(hei, wei):

    bmi = round(wei / (hei ** 2))

    if bmi < 18.5:
        return f" Your bmi  is {bmi},you are under weight"
    elif 18.5 < bmi < 25:
        return f" Your bmi  is {bmi},your weight is Normal"
    elif 25 < bmi < 30:
        return f" Your bmi  is {bmi},you are Overweight"
    elif 30 < bmi < 35:
        return f" Your bmi  is {bmi},you are Obese"
    else:
        return f" Your bmi  is {bmi},you are Clinically Obese"


height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

james = bmi_calc(height, weight)
