income = float(input("Enter the annual income: "))

if income < 85528:
    tax = income * 0.18 - 556.02
# Write the rest of your code here.
elif income > 85528:
        excess_income = income - 85528
        tax = excess_income * 0.32 + 14839.02
if tax <= 0:
    tax = 0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")