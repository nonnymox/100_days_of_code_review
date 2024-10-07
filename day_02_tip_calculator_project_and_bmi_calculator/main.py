# BMI CALCULATOR
# height = 1.65
# weight = 84
#
# # Write your code here.
# # Calculate the bmi using weight and height.
# bmi = weight / height**2
#
# print(bmi)

# Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = float(input("How much tip would you like to give? 10, 12 or 15?  "))
tip = tip_percent/100 * bill
bill += tip
people = float(input("How many people to split the bill? "))
individual_bill = bill/people
print(f"Each person should pay: ${individual_bill:.2f}")
