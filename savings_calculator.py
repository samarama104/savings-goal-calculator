import math

goal = float(input("Savings goal ($): "))
current = float(input("Current savings ($): "))
contribution = float(input("Monthly contribution ($): "))

if goal < 0 or current < 0 or contribution < 0:
    print("Amounts cannot be negative.")
elif current >= goal:
    print("You've already reached your savings goal!")
elif contribution == 0:
    print("Monthly contribution must be greater than zero.")
else:
    remaining = goal - current
    months = math.ceil(remaining / contribution)

    print(f"Remaining to save: ${remaining:.2f}")
    print("Months needed:", months)